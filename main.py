"""
RAG + 知识图谱系统主程序
功能：完整的RAG流程入口点
"""

import json
from pathlib import Path
from datetime import datetime
from pipeline import CompleteRAGPipeline


def main():
    """主函数"""
    # 配置
    USE_OPENAI = False  # 设置为True以使用OpenAI模型
    USE_VLLM = True  # 设置为True以使用vLLM（默认）
    OPENAI_API_KEY = None  # 如果使用OpenAI，请设置API密钥
    VLLM_BASE_URL = "http://127.0.0.1:8910/v1"  # vLLM服务地址
    VLLM_MODEL_NAME = None  # vLLM模型名称（None表示自动获取）
    
    # 创建流程管道
    pipeline = CompleteRAGPipeline(
        use_openai=USE_OPENAI,
        api_key=OPENAI_API_KEY,
        use_vllm=USE_VLLM,
        vllm_base_url=VLLM_BASE_URL,
        vllm_model_name=VLLM_MODEL_NAME
    )
    
    # 指定Markdown文件或目录路径
    markdown_root = Path(__file__).resolve().parent / "AI_database_markdown"
    # 如果AI_database_markdown目录存在，使用它；否则可以指定其他markdown文件路径
    if markdown_root.exists():
        markdown_paths = [str(markdown_root)]
    else:
        raise FileNotFoundError(f"AI_database_markdown目录不存在: {markdown_root}")

    
    use_existing = input("是否直接使用已有向量库进行检索？(Y/N): ").strip().upper()
    if use_existing == "Y":
        pipeline.prepare_from_existing_vectorstore()
    else:
        pipeline.run_from_markdown(markdown_inputs=markdown_paths)
    
    # 测试问答
    test_questions = [
        "2024 年，株洲中车时代电气股份有限公司中标金额是多少？",
        "根据欧洲铁路局 2025-2027 年单一规划文件，机构注册系统迁移到知识图谱（knowledge graph）方法的目标进度在 2025 年底应达到多少百分比？",
        "在 UIC 的报告里，根据国际能源署的分析，铁路的市场份额需要增长多少才能在本十年内实现《巴黎协定》的目标？",
        "参照 IEEE 1474.1 的定义，附件 D (Typical safe braking model) 中对安全制动模型的描述，在“滑行时间 (Coast time, C)”期间，列车被假定处于什么状态？",
        "在 Manresa 车站的事件调查报告中，列车 78443 被授权越过 3023 进站信号机后，何时（日期和时间）发生了列车 95218 最终启动了行驶，并最终导致两列车存在碰撞风险？",
        "南京地铁 S7 号线的运营里程，在江苏省内已运营地铁长度中排第几？",
        "车辆外部移动实体的场景要素：根据 GB/T 43267—2023（预期功能安全），在场景要素结构中，可移动实体的第 2 层要素和第 3 层要素分别是什么？（需完整列出第 3 层中所有实体类型）",
        "根据文档《2024_Communications-Based Train Control》，图 5.11 所示的网状控制回路结构，ATO 子系统是如何实现自身的控制回路的？请阐述其如何获取输入（Messglieder），如何形成车辆轨迹（Fahrzeugtrajektorie），以及如何将轨迹作为目标值传递给列车的控制设备（Steuergerät）？",
        "在 CBTC 互联互通规范体系中，关于列车启动、加速、巡航和制动的自动控制功能，其在《系统总体要求》中的分配归属于哪个子系统？并在《CBTC 部分测试及验证》中体现在哪个功能的测试中，测试需求编号是什么？",
        "ERTMS/ETCS 列车牵引系统数据定义演变：比较 SUBSET-026 Baseline 3 (v3.4.0) 和 Baseline 4 (v4.0.0) 版本中 Validated Train Data (Packet 11) 的内容定义：1）请指出该数据包中用于表示牵引系统标识的变量名称？2）当该变量不为零时，需要包含哪些额外的牵引数据变量？"
    ]
    
    items = []
    for question in test_questions:
        result = pipeline.answer_question(question)
        contexts = []
        source_docs = result.get("source_documents") or []
        for doc in source_docs:
            page_content = getattr(doc, "page_content", None)
            if page_content:
                contexts.append(page_content)
        items.append({
            "question": question,
            "retrieved_contexts": contexts,
            "answer": result.get("answer")
        })
    
    output = {"items": items}
    print(json.dumps(output, ensure_ascii=False, indent=2))
    
    # 保存JSON文件到output目录
    output_dir = Path(__file__).resolve().parent / "output"
    output_dir.mkdir(exist_ok=True)
    
    # 生成带时间戳的文件名
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"output_{timestamp}.json"
    
    # 保存JSON文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"\n结果已保存到: {output_file}")
    
    # 启动交互式问答
    # pipeline.interactive_qa()


if __name__ == "__main__":
    main()

