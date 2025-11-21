# 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范第2部分：系统架构和功能分配

# Urban rail transit — System specification for interoperability of communication based train control system

# Part 2: System architecture and functional allocations

2018-09-10 发布

2018-12-31 实施

# 目次

前言 V  
引言 VIII

1 范围 1  
2 规范性引用文件

3 术语和缩略语

3.1 术语 2  
3.2 缩略语 5

4 系统架构 5

4.1 架构组成 5  
4.2 CBTC系统物理接口和功能接口 5

5 功能对照  
6 ATP功能分配 10

6.1 ATP的主要功能 10  
6.2 列车位置确定 12  
6.3 移动防护限制和目标点的确定 19  
6.4 ATP曲线确定 24  
6.5 确定限制速度 27  
6.6 列车实际速度/列车运行方向确定 28  
6.7 监督/强制允许速度和允许运行方向 30  
6.8 车门/站台门控制 33  
6.9 列车折返 38  
6.10 车载ATP用户界面 39  
6.11 自诊断、故障报警及数据记录 40

# 7 ATO功能分配 40

7.1 功能描述 40  
7.2 确定ATO曲线 40  
7.3 列车速度调整 42  
7.4 门控制 43  
7.5 车载ATO用户界面 45  
7.6 自诊断、故障报警及数据记录 45

# 8 ATS功能分配 46

8.1 功能描述 46  
8.2 列车识别 46  
8.3 列车追踪 48  
8.4 列车进路办理 48  
8.5 列车调整 50  
8.6 列车运行控制 51  
8.7 控制列车运行 53  
8.8 时刻表编制· 53  
8.9 模拟培训 53  
8.10 用户界面 54

# 9 CI功能分配 56

9.1 功能描述 56  
9.2 进路办理 56  
9.3 锁闭/解锁进路/区段 58  
9.4 紧急停车按钮 59  
9.5 故障监测及操作记录 59

# 参考文献 61

# 前言

T/CAMET04010《城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通系统规范》分为以下四个部分：

——第1部分：系统总体要求；  
——第2部分：系统架构和功能分配；  
——第3部分：车载电子地图；  
——第4部分：互联互通危害分析。

本部分是T/CAMET04010的第2部分。

本部分按照GB/T1.1—2009给出的规则起草。

请注意本部分的某些内容可能涉及专利，本部分的发布机构不承担识别这些专利的责任。

本部分由中国城市轨道交通协会技术装备专业委员会提出。

本部分由中国城市轨道交通协会归口。

本部分起草单位：交控科技股份有限公司、北京交通大学、北京全路通信信号研究设计院集团有限公司、中国铁道科学研究院集团有限公司通信信号研究所、株洲中车时代电气股份有限公司、浙江众合科技股份有限公司。

本部分主要起草人：编写组：郜春海、黄友能、王伟、刘波、李凯、王悉、刘宏杰、孙晓光、刘鲁鹏、吕浩炯、刘志水、尹逊政、孙旺、高晓菲、胡顺定。审查组：李中浩、朱翔、赵炜、郑生全、张艳兵、张良、王道敏、张琼燕、段晨宁、李新文、李德堂、文成祥、任敬、朱东飞、肖利君、张守芝、刘新平。

# 引言

为促进中国城市轨道交通建设，实现并满足城市轨道交通互联互通的需要，达到经济适用、资源共享、技术先进及可持续发展的目标，制定城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系列团体标准。

该系列规范包括《城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通系统规范》、《城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通接口规范》、《城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通测试规范》《城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通工程规范》4个规范(17个部分)。

# 城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通系统规范第2部分：系统架构和功能分配

# 1 范围

T/CAMET04010的本部分定义了互联互通的系统架构和功能分配技术要求，包括互联互通下CBTC系统的物理接口和功能接口，以及ATP、ATO、ATS、CI各系统的功能分配。

本部分适用于国内采用基于通信的列车运行控制（CBTC）系统的新建、更新改造及扩建的城市轨道交通线路建设，用于指导信号系统的系统设计、产品设计、设备招标、工程建设。

# 2 规范性引用文件

下列文件对于本部分的应用是必不可少的。凡是注日期的引用文件，仅所注日期的版本适用于本部分。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本部分。

GB/T12758—2004 城市轨道交通信号系统通用技术条件

GB50157—2013 地铁设计规范

CJ/T407—2012城市轨道交通基于通信的列车自动控制系统技术要求

T/CAMET 04010.1—2018 城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通系统规范 第1部分：系统总体要求

# 3 术语和缩略语

GB/T12758—2004、GB50157—2013、CJ/T407—2012和T/CAMET

04010.1—2018界定的及下列术语和缩略语适用于本部分。为了便于使用，以下重复列出了其中的主要相关术语。

# 3.1 术语

3.1.1

# 城市轨道交通信号 urban rail transit signal

应用于城市轨道交通系统中，人工或自动实现行车指挥和列车运行控制、安全间隔控制技术的总称。

[GB/T12758—2004，术语与定义3.1]

3.1.2

基于通信的列车控制 communication based train control (CBTC)

通过不依赖轨旁列车占用检测设备的列车主动定位技术，连续车-地双向数据通信技术以及能够执行安全功能的车载和地面处理器而构建的连续式列车自动控制系统。

[CJ/T407—2012，定义3.1.1]

3.1.3

# 移动闭塞 moving block

前方列车与后续列车之间的最小安全追踪间隔距离单元不预定设定，并随列车的移动、速度的变化而变化的闭塞方式。

[GB/T12758—2004术语与定义3.10]

3.1.4

# 列车自动控制 automatic train control

信号系统自动实现列车监控、安全防护和运行控制等技术的总称。

[GB50157—2013，定义2.0.37]

3.1.5

# 列车自动监控 automatic train supervision

根据列车时刻表为列车运行自动设定进路、指挥行车、实施列车运行管理等技术的总称。

[GB50157—2013，定义2.0.38]

# 3.1.6

列车自动防护 automatic train protection

自动实现列车运行间隔、超速防护、进路安全和车门等监控技术的总称。

[GB50157—2013，定义2.0.39]

# 3.1.7

列车自动运行 automatic train operation

自动实现列车加速、调速、停车和车门开闭、提示等控制技术的总称。

[GB50157—2013，定义2.0.40]

# 3.1.8

计算机联锁 computer interlocking

以计算机技术为核心，自动实现进路、道岔、信号机等防护技术的总称。

[CJ/T407—2012，定义3.1.6]

# 3.1.9

维护支持系统 maintenance support system

监测记录系统内其他各子系统维护信息，辅助系统故障分析，用于系统日常运营维护

# 3.1.10

保护区段 overlap section

为实现超速防护，保证安全停车而延伸的闭塞区段。

[GB/T12758—2004，术语与定义3.12]

# 3.1.11

目标速度 target speed

列车运行至前方目标地点应达到的允许速度。

[GB/T12758—2004，术语与定义3.13]

# 3.1.12

目标距离 target distance

列车运行至前方目标地点的走行距离。

[GB/T12758—2004，术语与定义3.14]

3.1.13

# 安全保护距离 safe protection distance

列车自动防护系统中，列车超速防护实施安全停车控制时，为防止停车位置离散性可能造成的危险，而设置的自预定停车位置至目标地点的安全距离。

[GB/T12758—2004，术语与定义3.15]

3.1.14

# 危险点 danger point

列车运行前方不允许列车任何部位越过的特定点。

[T/CAMET04010.1,术语和缩略语3.1.10]

3.1.15

# 移动授权 movement authority

列车沿给定的行驶方向进入并在某一特定轨道区段内行车的许可。

[CJ/T407—2012，定义3.1.7]

3.1.16

# 限制速度 restricted speed

线路、车辆结构等限制及列车移动授权所获取的最严格的速度限制。

[CJ/T407—2012，定义3.1.11]

3.1.17

# 互联互通 interoperability

装备不同信号厂家车载设备的列车可以在装备不同信号厂家轨旁设备的一条轨道交通线路内或多条轨道交通线路上无缝互通、安全可靠运营。

[T/CAMET 04010.1,术语和缩略语3.1.16]

3.1.18

# 共线运行 mix operation

装备不同厂家车载信号设备的列车可以在装备同一厂家轨旁信号设

备线路上支持以点式列车控制级别和连续式列车控制级别无缝安全可靠运营。

# 3.2 缩略语

AM：列车自动驾驶模式（Automatic Train Operating Mode）

ATC：列车自动控制（Automatic Train Control）

ATO：列车自动运行（Automatic Train Operation）

ATP：列车自动防护（Automatic Train Protection）

ATS：列车自动监控（Automatic Train Supervision）

CBTC：基于通信的列车控制系统（Communication Based Train Control）

Cl:计算机联锁（Computer Interlocking）

CM：列车自动防护模式（Code Train Operating Mode）

DCS:数据通信系统(Data Communication System)

LEU：轨旁电子单元（Lineside Electronic Unit）

MSS：维护支持子系统（Maintenance Support System）

RM：限制人工驾驶模式（Restricted Train Operating Mode）

SIL：安全完整性等级（Safety Integrity Level）

ZC：区域控制器（ZoneController）

# 4 系统架构

# 4.1 架构组成

CBTC系统由ATS、CBTC轨旁（轨旁CBTC设备，含区域控制器等）、CBTC车载（车载CBTC设备，含车载ATP、车载ATO等）、CI、DCS子系统组成。

# 4.2 CBTC系统物理接口和功能接口

CBTC系统物理接口和功能接口示意图见图1，互联互通下CBTC系统物理接口和功能接口示意图见图2。

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/69683818-e6f1-4336-ad86-85967153f544/ab39b485a259aa01eb01c97dbbae99a1ee36b462af67fde64e750dce9258a79f.jpg)  
图1CBTC系统物理接口和功能接口示意图

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/69683818-e6f1-4336-ad86-85967153f544/52d1d56bbdfb2fdc3723811a08160d966d78e85051897159947bd897d6916d4a.jpg)  
图2 互联互通下CBTC系统物理接口和功能接口示意图

相对于CBTC系统物理接口和功能接口，互联互通下CBTC系统物理接口和功能接口，增加了列车与邻线地面设备间的接口，以及各线间地面设备间的接口（CBTC轨旁间及CI设备间）。

# 5 功能对照

功能分配与总体要求的对照内容见表1。

表 1 功能对照表  

<table><tr><td>序号</td><td>总体要求中的功能点名称</td><td>对应本文章节</td></tr><tr><td>1</td><td>初始化 CBTC 列车位置</td><td>6.2.2</td></tr><tr><td>2</td><td>确定 CBTC 列车位置</td><td>6.2.3</td></tr><tr><td>3</td><td>确定轨道区段占用状态</td><td>6.2.4</td></tr><tr><td>4</td><td>防护列车丢失位置报告</td><td>6.2.5.2</td></tr><tr><td>5</td><td>防护列车完整性丢失</td><td>6.2.5.3</td></tr><tr><td>6</td><td>确定前方 CBTC 列车位置</td><td>6.3.2.2</td></tr><tr><td>7</td><td>确定前方安全进路限制</td><td>6.3.2.3</td></tr><tr><td>8</td><td>确定移动授权</td><td>6.3.3.2</td></tr><tr><td>9</td><td>确定目标点</td><td>6.3.4.2</td></tr><tr><td>10</td><td>响应紧急停车按钮</td><td>6.3.4.3</td></tr><tr><td>11</td><td>道岔状态防护</td><td>6.3.4.4</td></tr><tr><td>12</td><td>车载故障处理</td><td>6.3.5.2</td></tr><tr><td>13</td><td>固定速度限制防护</td><td>6.4.2</td></tr><tr><td>14</td><td>临时限速限制防护</td><td>6.4.3</td></tr><tr><td>15</td><td>确定制动曲线</td><td>6.4.4</td></tr><tr><td>16</td><td>列车超速防护</td><td>6.4.4.3</td></tr><tr><td>17</td><td>列车速度测定</td><td>6.6.2</td></tr><tr><td>18</td><td>测速误差补偿</td><td>6.6.2.3</td></tr><tr><td>19</td><td>零速状态确定</td><td>6.6.2.4</td></tr><tr><td>20</td><td>列车运行方向确定</td><td>6.6.3</td></tr><tr><td>21</td><td>列车运行方向防护</td><td>6.7.3.2</td></tr><tr><td>22</td><td>退行防护</td><td>6.7.3.3</td></tr><tr><td>23</td><td>越过移动授权终点防护</td><td>6.7.4.1</td></tr><tr><td>24</td><td>移动授权更新超时防护</td><td>6.7.4.3</td></tr><tr><td>25</td><td>紧急制动缓解</td><td>6.7.4.4</td></tr><tr><td>26</td><td>车门允许</td><td>6.8.2</td></tr><tr><td>27</td><td>站台门控制</td><td>6.8.2.3</td></tr><tr><td>28</td><td>车门防护</td><td>6.8.3.2</td></tr><tr><td>29</td><td>车门防护切除</td><td>6.8.4.4</td></tr><tr><td>30</td><td>站台门防护</td><td>6.8.3</td></tr><tr><td>31</td><td>列车折返</td><td>6.9</td></tr><tr><td>32</td><td>车载ATP界面功能</td><td>6.10.1</td></tr><tr><td>33</td><td>ATP自诊断、故障报警及数据记录</td><td>6.11</td></tr><tr><td>34</td><td>模式转换</td><td>6.2.3.10</td></tr><tr><td>35</td><td>ZC间移交</td><td>6.3.4.5</td></tr><tr><td>36</td><td>电子地图存储</td><td>6.2.2.4</td></tr><tr><td>37</td><td>停稳停准判断</td><td>6.2.3.8</td></tr><tr><td>38</td><td>确定ATO曲线</td><td>7.2.1</td></tr><tr><td>39</td><td>精确停车</td><td>7.2.2</td></tr><tr><td>40</td><td>根据ATO曲线调整列车速度</td><td>7.3.1</td></tr><tr><td>41</td><td>跳停</td><td>7.3.2</td></tr><tr><td>42</td><td>运营调整</td><td>7.3.3</td></tr><tr><td>43</td><td>开关车门</td><td>7.4.1.1</td></tr><tr><td>44</td><td>ATO界面显示</td><td>7.5</td></tr><tr><td>45</td><td>ATO自诊断故障报警及数据记录</td><td>7.6.2</td></tr><tr><td>46</td><td>ATO发送列车运行信息</td><td>7.3.4</td></tr><tr><td>47</td><td>ATO发送旅客信息</td><td>7.6.3</td></tr><tr><td>48</td><td>确定列车识别号</td><td>8.2</td></tr><tr><td>49</td><td>ATS列车追踪</td><td>8.3</td></tr><tr><td>50</td><td>列车进路办理</td><td>8.4</td></tr><tr><td>51</td><td>列车自动调整</td><td>8.5.1</td></tr><tr><td>52</td><td>节能运行</td><td>8.5.2</td></tr><tr><td>53</td><td>扣车</td><td>8.6.1</td></tr><tr><td>54</td><td>提前发车</td><td>8.6.2</td></tr><tr><td>55</td><td>跳停</td><td>8.6.3</td></tr><tr><td>56</td><td>设置/取消临时限速</td><td>8.7</td></tr><tr><td>57</td><td>时刻表编制管理</td><td>8.8</td></tr><tr><td>58</td><td>模拟培训</td><td>8.9</td></tr><tr><td>59</td><td>ATS界面功能</td><td>8.10.1</td></tr><tr><td>60</td><td>ATS数据记录</td><td>8.10.2.4</td></tr><tr><td>61</td><td>中控/站控转换</td><td>8.6.4</td></tr><tr><td>62</td><td>进路办理</td><td>9.2.2</td></tr><tr><td>63</td><td>保护区段建立</td><td>9.2.4</td></tr><tr><td>64</td><td>进路/区段锁闭</td><td>9.3.2</td></tr><tr><td>65</td><td>道岔单操、单锁</td><td>9.3.3</td></tr><tr><td>66</td><td>车站/区间封锁</td><td>9.3.2</td></tr><tr><td>67</td><td>紧急停车按钮</td><td>9.4</td></tr><tr><td>68</td><td>CI接口</td><td>无</td></tr><tr><td>69</td><td>CI自检、故障报警及数据记录</td><td>9.5</td></tr><tr><td>70</td><td>进路解锁及取消</td><td>9.3.2</td></tr><tr><td>71</td><td>计轴故障恢复</td><td>9.3.4</td></tr><tr><td>72</td><td>扣车</td><td>8.6.1</td></tr><tr><td>73</td><td>站控/遥控</td><td>8.6.4</td></tr><tr><td>74</td><td>CI权限设置</td><td>无</td></tr></table>

# 6 ATP功能分配

# 6.1 ATP的主要功能

ATP的主要功能见图3。

图3 ATP主要功能  
![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/69683818-e6f1-4336-ad86-85967153f544/71aeefc53de79539751f68da1d1ab3b8b902301987c1a0a42918ce3f465d62e5.jpg)  
说明：  
实线框——其他章节描述内容；  
虚线框——本章节描述内容。

# 6.2 列车位置确定

# 6.2.1 确定列车位置关系图

图4概括了本段中所描述的子功能(实线框)之间的接口，以及其他段落中描述的子功能(虚线框)间的接口。

图4 确定列车位置关系图  
![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/69683818-e6f1-4336-ad86-85967153f544/cfc6776e400ad17be6e1ad0dc34eb99700dbe2c1d8c00881bff2e3fe4aba82c0.jpg)  
说明：  
实线框——定位功能的条件；  
虚线框——定位功能的用途

# 6.2.2 初始化CBTC列车位置

# 6.2.2.1 概述

此功能用于初始化CBTC列车位置，即确定CBTC装备列车的初始位置。表2～表4规定了列车定位初始化的内容。

# 6.2.2.2 进入CBTC区域的CBTC列车位置初始化

CBTC列车位置初始化，并自动检测每列符合装备CBTC设备的列车，进入CBTC区域无需手动输入列车位置或列车长度的数据，见表2。

表 2 进入 CBTC 区域的 CBTC 列车位置初始化  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC 轨旁</td><td>X</td><td></td><td></td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td>X</td></tr><tr><td colspan="4">注1:“输入”为该功能提供输入的子系统;“实现”该功能的子系统;“输出”接收该功能实现结果的子系统(适用于后续表格的内容)注2:本表格及后续表格中的“CBTC 轨旁”包含“CBTC 轨旁、应答器、LEU”</td></tr></table>

# 6.2.2.3 从设备故障中恢复的CBTC列车完成位置初始化

CBTC列车位置初始化，并应自动检测每列装备CBTC设备的列车，从CBTC设备故障中恢复的列车无需手动输入列车位置或列车长度的数据，见表3。

表 3 进从设备故障中恢复的 CBTC 列车完成位置初始化  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td>X</td><td></td><td></td></tr><tr><td>CBTC车载</td><td></td><td>X</td><td>X</td></tr></table>

# 6.2.2.4 电子地图存储

CBTC系统的车载设备和轨旁设备应根据运行和管辖范围的不同，分别存储相关线路范围的电子地图，见表4。

表 4 电子地图存储  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC 轨旁</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 6.2.3 确定CBTC列车位置

# 6.2.3.1 概述

此功能确定列车运行前方和后方的相邻CBTC列车的位置。表5～表13规定了列车位置用途的内容。

# 6.2.3.2 确定列车长度

CBTC列车位置应能确定列车长度，见表5。

表 5 确定列车长度  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td>X</td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td></td></tr></table>

# 6.2.3.3 确定CBTC列车位置

CBTC列车位置的确定应包括安全、准确地确定列车车头和车尾的位置，并用足够的分辨率和精准度来满足性能和安全需求，见表6。

表 6 确定 CBT 列车位置  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC轨旁</td><td>X</td><td></td><td>X</td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 6.2.3.4 位置误差校正

CBTC列车位置的确定应包含测距误差的影响，并对位置误差包含合适的余量，见表7。

表 7 位置误差校正  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td>X</td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 6.2.3.5 列车完整性检测

CBTC系统应能实现列车的完整性检测，当车载设备检测到列车完整性信息丢失，列车完整性检查电路中断时，应对列车实施紧急制动，并丢失定位，同时系统应对后续追踪列车进行安全防护，保证后续列车安全运行，见表8。

表 8 列车完整性检测  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td>X</td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td></td></tr><tr><td>CI</td><td></td><td></td><td></td></tr><tr><td>外部系统(车辆)</td><td>X</td><td></td><td></td></tr></table>

# 6.2.3.6 列车轮径校正

CBTC系统应能实现列车轮径校正功能，系统宜在列车进入转换轨前设置轮径自动补偿设备，并在出段/场前完成自动轮径补偿，见表9。

表 9 列车轮径校正  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC 轨旁</td><td>X</td><td></td><td></td></tr><tr><td>CBTC 车载</td><td></td><td>X</td><td>X</td></tr></table>

# 6.2.3.7 列车升级至CBTC级别

当系统由点式列车控制级别或联锁控制级别升级为连续式列车控制级别时，应满足如下转换条件：

——ATP 车载设备无故障，且完成列车定位；

——ATP 车载设备收到 ATP 轨旁设备发送的有效 MA 信息，见表 10。

表 10 列车升级至 CBTC 级别  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC 轨旁</td><td></td><td>X</td><td></td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CI</td><td>X</td><td></td><td>X</td></tr></table>

# 6.2.3.8 确定列车停站位置

CBTC系统应根据不同的列车长度，确定列车的停站位置，见表11。

表 11 确定列车停站位置  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 6.2.3.9 列车驾驶模式

列车应具有的驾驶模式包括：列车自动运行模式（AM）、列车自动防护模式（CM）、限制人工驾驶模式（RM）、非限制人工驾驶模式（EUM）、列车自动运行模式（AM），列车自动防护模式（CM）为列车正常运行模式，见表12。

表 12 列车驾驶模式  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td>X</td></tr><tr><td>CBTC车载</td><td></td><td></td><td>X</td></tr></table>

# 6.2.3.10 驾驶模式转换

列车驾驶模式等级由高至低分别为：AM、CM、RM，各驾驶模式满足转换条件可由人工转换，也可自动转换，车载设备应予以记录和显示。

为保证行车安全，列车驾驶模式由AM、CM转换为RM时，列车应停车，驾驶模式由低等级向高等级转换时，列车宜不停车转换驾驶模式，见表13。

表 13 驾驶模式转换  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 6.2.4 确定轨道区段占用状态

# 6.2.4.1 概述

此功能用于确定轨道区段的占用状态。表14和表15规定了轨道区段占用状态的内容：

# 6.2.4.2 轨道区段的占用状态

CBTC系统可根据轨旁次级占用检测设备提供的信息，结合CBTC列车汇报的位置信息，确定轨道区段的占用状态（有一辆或多辆车占用区段，包括CBTC列车和(或)装有无效的CBTC车载设备的列车）见表14。

表 14 轨道区段的占用状态  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC 轨旁</td><td></td><td>X</td><td>X</td></tr><tr><td>CBTC 车载</td><td>X</td><td></td><td></td></tr><tr><td>CI</td><td>X</td><td>X</td><td></td></tr><tr><td>外部系统(次级占用检测设备)</td><td>X</td><td></td><td></td></tr></table>

# 6.2.4.3 前方轨道区段占用状态

当CBTC列车前方区段被故障列车或者非CBTC装备列车占用时，CBTC系统应根据前方区段占用状态确定CBTC列车的安全边界，见表15。

表 15 前方轨道区段的占用状态  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td>X</td><td></td></tr><tr><td>CBTC车载</td><td></td><td></td><td>X</td></tr><tr><td>CI</td><td>X</td><td></td><td></td></tr></table>

# 6.2.5 故障管理

# 6.2.5.1 概述

与基础的CBTC系统功能组合，后备轨旁系统和/或操作程序应在确

定列车位置功能故障情况下，为列车移动提供安全保障。表16和表17规定了列车位置功能故障的内容。

# 6.2.5.2 防护列车丢失位置报告

当列车丢失位置报告后，CBTC系统将提供移动授权防护，避免其他列车进入无位置汇报列车占用的区段，见表16。

表 16 防护列车丢失位置报告  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td>X</td><td>X</td></tr><tr><td>CBTC车载</td><td>X</td><td></td><td></td></tr><tr><td>CI</td><td>X</td><td></td><td></td></tr></table>

# 6.2.5.3 列车完整性丢失防护

在检测到列车完整性丢失时，CBTC系统将提供移动授权防护，避免其他列车进入无位置汇报列车占用的区段，见表17。

表 17 列车完整性丢失防护  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>CBTC ATS 设备</td><td></td><td></td><td></td></tr><tr><td>CBTC 轨旁</td><td></td><td>X</td><td>X</td></tr><tr><td>CBT 车载</td><td>X</td><td>X</td><td></td></tr><tr><td>CI</td><td>X</td><td></td><td></td></tr></table>

# 6.3 移动防护限制和目标点的确定

# 6.3.1 移动防护限制和相关的目标点

这一功能为CBTC列车确立了移动防护限制和相关的目标点。图5为移动保护的限定和目标点测定。

图5 移动保护的限定和目标点测定  
![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/69683818-e6f1-4336-ad86-85967153f544/8824c7095ea36110dd27ed2287bbf7850db1aedb5fad790af0a5f71e2b549b5a.jpg)  
说明：  
实线框——移动授权确定的具体条件；  
虚线框——移动授权保护的限定和失效防护

# 6.3.2 确定移动防护的潜在限制

# 6.3.2.1 功能描述

此功能用于确定CBTC列车前方移动授权的限制。表18和表19规定了列车位置用途的内容。

# 6.3.2.2 CBTC列车前方位置

对于每辆CBTC列车，应确定列车前方的CBTC列车位置，见表18。

表 18 CBTC 列车前方位置  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td>X</td><td>X</td></tr><tr><td>CBTC车载</td><td>X</td><td></td><td>X</td></tr></table>

# 6.3.2.3 前方安全进路限制

对于每辆CBTC列车，系统应确定列车的安全进路位置，见表19。

表 19 前方安全进路限制  

<table><tr><td>功能分配</td><td>输 入</td><td>实 现</td><td>输 出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC 轨旁</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CBTC 车载</td><td></td><td></td><td>X</td></tr><tr><td>CI</td><td>X</td><td></td><td></td></tr></table>

# 6.3.3 移动授权的确定

# 6.3.3.1 概述

此功能确定移动授权。表20规定了移动授权的内容

# 6.3.3.2 移动授权的确定

为对列车进行合适的移动防护限制，CBTC系统应估算最大移动授权限制位置，见表20。

表 20 移动授权的确定  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC轨旁</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CBTC车载</td><td></td><td>X</td><td>X</td></tr><tr><td>CI</td><td>X</td><td></td><td></td></tr></table>

# 6.3.4 目标点确定

# 6.3.4.1 概述

此功能确定移动防护限制的目标点。表21～表24规定了目标点的内容。

# 6.3.4.2 目标点确定

为了确保列车不超过移动授权，CBTC系统应确定一个目标点，见表21。

表 21 目标点确定  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td>X</td><td>X</td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CI</td><td>X</td><td></td><td></td></tr></table>

# 6.3.4.3 响应紧急停车按钮的按下

当ATP轨旁设备接收到站台紧急停车按钮被按下的信息时，应通过车地通信设备向列车发送相应的列车控制命令信息，见表22。

表 22 响应紧急停车按钮的按下  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC轨旁</td><td></td><td>X</td><td></td></tr><tr><td>CBTC车载</td><td></td><td>X</td><td>X</td></tr><tr><td>CI</td><td>X</td><td></td><td></td></tr></table>

# 6.3.4.4 道岔状态防护

CBTC系统应控制区域内道岔状态并进行防护。当道岔状态丢失时，移动授权回撤至道岔区域的边界位置；当列车已驶入丢失状态的道岔

区域时，列车应实施紧急制动，见表23。

表 23 道岔状态保护  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td>X</td><td></td></tr><tr><td>CBTC车载</td><td></td><td></td><td>X</td></tr><tr><td>CI</td><td>X</td><td></td><td></td></tr></table>

# 6.3.4.5 ZC切换

两条连续式列车控制级别线路间应设置移交边界和移交重叠区。

列车进入移交重叠区后，车载ATP设备应同时与移交、接管线路的轨旁ATP设备建立通信，并根据列车是否越过移交边界选择采用移交/接管线路的轨旁ATP设备发送的MA；移交、接管线路的轨旁ATP设备间应互传线路状态、列车位置等信息，并向车载ATP设备发送MA信息，见表24。

表 24 ZC 切换  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td></td><td></td></tr><tr><td>CBTC 轨旁</td><td></td><td>X</td><td></td></tr><tr><td>CBTC 车载</td><td></td><td>X</td><td>X</td></tr><tr><td>CI</td><td>X</td><td></td><td></td></tr></table>

# 6.3.5 故障管理

# 6.3.5.1 概述

本功能明确ATP故障管理的要求。表25规定了故障管理的内容。

# 6.3.5.2 故障管理

列车的非预期移动、ATP轨旁设备故障、车载设备故障、超过系统允

许范围的车地通信中断等均应给出报警提示，与行车安全相关的故障均应产生紧急制动，见表25.

表 25 故障管理  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC轨旁</td><td>X</td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CI</td><td></td><td></td><td></td></tr></table>

# 6.4 ATP曲线确定

# 6.4.1 ATP曲线计算

该功能用于计算ATP曲线，如图6所示。

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/69683818-e6f1-4336-ad86-85967153f544/7d9dfbd27ac75d5501f7bb848792a51cb011de103a119f73a286f4ab2def1fd3.jpg)  
图6 ATP曲线计算

# 6.4.2 固定限制速度防护

此功能确定列车的固定限制速度。表26和表27规定了固定限制速度防护。

# 6.4.2.1 固定线路限制速度

CBTC应提供固定线路限速的限制防护，见表26。

表 26 固定线路限制速度  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC 轨旁</td><td>X</td><td>X</td><td></td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CI</td><td>X</td><td></td><td></td></tr></table>

# 6.4.2.2 列车构造限制速度

系统应提供列车构造速度的防护，见表27。

表 27 列车构造限制速度  

<table><tr><td>功能分配</td><td>输 入</td><td>实 现</td><td>输 出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td></td><td></td><td></td></tr></table>

# 6.4.3 临时限速限制防护

# 6.4.3.1 概述

此功能确定列车的临时限速防护。表28规定了临时限速限制防护问题。

# 6.4.3.2 临时限制速度限制

CBTC应按照系统设置的临时限速，为列车计算移动授权，对临时限速进行防护，见表28。

表 28 临时限制速度限制  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CBTC车载</td><td></td><td>X</td><td>X</td></tr></table>

# 6.4.4 确定制动曲线

# 6.4.4.1 概述

此功能确定制动曲线，以保证列车在指定的目标点停车。表29和表30规定制动曲线的内容。

# 6.4.4.2 目标点的制动曲线

表 29 规定了目标点制动曲线的内容。

表 29 目标点的制动曲线  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC 轨旁</td><td>X</td><td></td><td></td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 6.4.4.3 防止制动曲线超过速度限制

CBTC应保证制动曲线在超过固定或临时限速之前减速，见表30。

表 30 防止制动曲线超过速度限制  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC 轨旁</td><td>X</td><td></td><td></td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 6.4.5 计算ATP曲线

# 6.4.5.1 概述

此功能用于计算完整的ATP曲线。表31规定了ATP曲线的内容。

# 6.4.5.2 ATP曲线

CBTC应为每辆列车计算完整的ATP曲线，见表31。

表 31 ATP 曲线  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td>X</td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 6.5 确定限制速度

# 6.5.1 CBTC列车限制速度

此功能确定对CBTC列车的限制速度。

图7概括了本条目描述的子功能接口和其他条目描述的子功能接口。

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/69683818-e6f1-4336-ad86-85967153f544/61466dce1d772bd1b0ac614826cff01c62176598d5085f4ecb77614589248a5e.jpg)  
图7 确定限制速度

# 6.5.2 确定限制速度

# 6.5.2.1 概述

此功能确定列车当前位置的限制速度。表32规定了限制速度的内容。

# 6.5.2.2 确定授权速度

CBTC应基于ATP曲线，确定列车当前位置的限制速度，见表32。

表 32 确定授权速度  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 6.6 列车实际速度/列车运行方向确定

# 6.6.1 概述

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/69683818-e6f1-4336-ad86-85967153f544/0e3010d98edb04e8647cdb1ad3d78d9d3ab5f98a84a9be28393c1b8b51bec941.jpg)  
图8概括了本条目描述的子功能接口和其他条目描述的子功能接口。  
图8 实际列车速度/运行方向确定

# 6.6.2 CBTC列车速度测定

# 6.6.2.1 概述

此功能确定列车的速度。表33～表35规定了CBTC列车速度测定的内容。

# 6.6.2.2 确定CBTC列车实际速度

CBTC应确定每辆CBTC装备列车的实际速度，速度满足分辨率和精度的要求，见表33。

表 33 确定 CBTC 列车实际速度  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 6.6.2.3 测速误差补偿

CBTC系统应能够补偿测速误差产生的影响，并对测速作出合适的补偿，见表34。

表 34 测速误差补偿  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 6.6.2.4 零速状态确定

CBTC应确定零速度状态，见表35。

表 35 零速状态确定  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td>X</td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CI</td><td></td><td></td><td>X</td></tr></table>

# 6.6.3 CBTC列车运行方向确定

# 6.6.3.1 概述

此功能确定列车实际运行方向。表36规定了CBTC列车运行方向。

# 6.6.3.2 确定CBTC列车运行方向

CBTC系统应确定每辆CBTC列车的实际运行方向，见表36。

表 36 确定 CBTC 列车运行方向  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td>X</td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CI</td><td></td><td></td><td></td></tr></table>

# 6.7 监督/强制允许速度和允许运行方向

# 6.7.1 功能描述

该功能是监督和强制执行允许速度和允许运行方向。

# 6.7.2 速度监督和防护

# 6.7.2.1 概述

此功能监督和防护列车速度，如图9所示。表37和表38规定了速度监督和防护的内容。

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/69683818-e6f1-4336-ad86-85967153f544/128f4afc3af4091ee5eb0d5aa5485e1f9504c9b0628ec4ffe71064d472a72963.jpg)  
图9 监督/施加授权速度和运行方向

# 6.7.2.2 速度监督和防护

如果列车实际速度超过限制速度，CBTC应实施紧急制动，见表37。

表 37 速度监督和防护  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 6.7.2.3 最不利情况下的影响

CBTC的速度监督/执行应包括对最差情况下系统偏差、反应次数和反应时间的补偿，见表38。

表 38 最不利情况下的影响  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 6.7.3 运行方向监督和防护

# 6.7.3.1 功能描述

此功能监督和防护列车运行方向。表39和表40规定了运行方向监督和防护的内容。

# 6.7.3.2 监督/防护运行方向

如果列车实际运行方向与授权的列车运行方向不一致，CBTC应实施紧急制动，见表39。

表 39 监督/防护运行方向  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC轨旁</td><td>X</td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 6.7.3.3 退行防护

ATP 车载设备应具有退行防护功能。当退行距离和退行速度超过允许值时，系统应立即采取紧急制动。在列车退行过程中，系统应对追踪运行的列车提供安全间隔防护。退行距离超过限制，车载设备应丢失定位，见表 40。

表40 退行防护  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td>X</td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 6.7.4 故障管理

# 6.7.4.1 越过移动授权终点的响应

系统应确保不会越过移动授权终点。表41～表44规定了故障管理的内容。

表 41 越过移动授权终点的响应  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC 轨旁</td><td>X</td><td></td><td></td></tr><tr><td>CBTC 车载</td><td></td><td>X</td><td>X</td></tr></table>

# 6.7.4.2 移动授权更新时的速度防护

移动授权更新时，如果列车的实际运行速度超过移动授权更新后的

紧急制动触发速度，系统应实施紧急制动。见表42。

表 42 移动授权更新的速度防护  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC轨旁</td><td>X</td><td></td><td></td></tr><tr><td>CBTC车载</td><td></td><td>X</td><td>X</td></tr></table>

# 6.7.4.3 移动授权更新超时的防护

移动授权更新超时，系统应实施紧急制动，见表43。

表 43 移动授权更新超时的防护  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC轨旁</td><td>X</td><td></td><td></td></tr><tr><td>CBTC车载</td><td></td><td>X</td><td>X</td></tr></table>

# 6.7.4.4 紧急制动缓解

在保证安全的条件下，系统可以缓解已施加的紧急制动，见表44。

表 44 紧急制动缓解  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 6.8 车门/站台门控制

# 6.8.1 功能描述

此功能实现车门/站台门控制，如图10所示。

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/69683818-e6f1-4336-ad86-85967153f544/7275629a20895694c2d65e59d809b5d04c198c0d5aecd35e19e0bbd6451a25a2.jpg)  
图10 车门/站台门控制

# 6.8.2 车门允许

# 6.8.2.1 概述

表  $45\sim$  表47规定了车门允许的内容。

# 6.8.2.2 车门允许

CBTC在开车门之前，应满足下列条件：

a）列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；  
b） 开门侧与站台一致；  
c） 列车零速；  
d）保持制动已施加。

列车在车站规定的位置停准停稳后，车载ATP应允许打开对应侧车门及站台门或双侧车门及站台门，并可选择通过自开自关、自开人关、人

开人关三种方式，自动或者人工打开车门。在AM驾驶模式下，可提供三种开门方式，CM驾驶模式下，仅能实现人工开门。见表45。

列车在车站停车超出停车窗范围，车载设备应不允许车门和站台门打开，司机可在车载设备防护条件下前进或后退，直至停车对位。

表45 车门允许  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 6.8.2.3 站台门控制

CBTC应打开站台门之前，应检查下列条件满足：

a) 列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；  
b)站台门侧与车门侧一致；  
c) 列车零速；  
d) 保持制动已施加。

控制内容见表46。

表 46 站台门控制  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td>X</td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CI</td><td></td><td></td><td>X</td></tr></table>

# 6.8.2.4 车门操作切除

车辆可以提供单个车门切除功能（全自动下），切除后的车门不响应

列车开门命令，见表47。

表 47 车门操作切除  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CI</td><td></td><td></td><td></td></tr><tr><td>外部系统(车辆)</td><td>X</td><td></td><td></td></tr></table>

# 6.8.3 车门、站台门防护

# 6.8.3.1 概述

表48和表49规定了车门和站台门防护的内容。

# 6.8.3.2 车门防护

仅在车门处于“关闭且锁闭”状态时，系统方允许列车移动，见表48。

表48 车门防护  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CI</td><td></td><td></td><td></td></tr></table>

# 6.8.3.3 站台门锁闭状态防护

仅在站台门处于“关闭且锁闭”状态时，系统方允许列车移动CBTC等级下，当站台门锁闭状态丢失时，还未进站的列车应根据接收到的移动授权，控制列车在站台前停车；已进站未停稳以及正在出站的列车应立即紧急制动；已完全出站的列车不受影响，见表49。

表 49 车门防护  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC 轨旁</td><td>X</td><td>X</td><td></td></tr><tr><td>CBTC 车载</td><td></td><td>X</td><td>X</td></tr><tr><td>CI</td><td>X</td><td></td><td></td></tr></table>

# 6.8.4 故障管理

# 6.8.4.1 概述

表  ${50} \sim$  表 52 规定了车间和站台门故障管理的内容。

# 6.8.4.2 车门状态丢失防护

列车在运行过程当中，车载设备应实时监督列车车门状态，当检测到车门不为关门且锁闭状态时，系统宜采取下列措施之一：

a）切除牵引但不实施制动；  
b）不切除牵引，也不实施制动，列车运行至下一座车站；  
c）实施紧急制动；  
d） 实施全常用制动

丢失防护内容见表50。

表 50 车门状态丢失防护  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 6.8.4.3 站台门状态丢失的响应

当列车靠近车站时或者列车已在站台区域时，站台门关闭状态丢失，CBTC系统采取保证列车安全的措施，见表51。

表 51 站台门状态丢失的响应  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td>X</td><td>X</td><td></td></tr><tr><td>CBTC车载</td><td></td><td>X</td><td>X</td></tr><tr><td>CI</td><td>X</td><td></td><td></td></tr></table>

# 6.8.4.4 车门防护切除

系统在车门故障时，可提供车门切除功能，此时ATP不再对车门状态进行防护，见表52。

表 52 车门防护切除  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CI</td><td></td><td></td><td></td></tr></table>

# 6.9 列车折返

列车折返方式应包括ATO无人自动折返模式、ATO有人自动折返模式、ATP监督下的人工折返模式。表53规定了列车折返方式的内容。

表 53 列车折返方式  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td>X</td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CI</td><td>X</td><td></td><td></td></tr></table>

# 6.10 车载ATP用户界面

# 6.10.1 CBTC车载ATP显示数据

表54规定了车载ATP显示数据界面的内容，CBTC车载显示屏幕显示ATP数据应包括：

a）列车运行模式；  
b）CBTC运行状态；  
c）当前列车速度；  
d）当前最大允许CBTC速度；  
e） 超速报警。

表 54 CBTC 车载 ATP 显示数据  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 6.10.2 CBTC车载ATP输入数据

表55规定了车载ATP输入数据的内容，用户ATP信息输入到CBTC应包括：

a）运行模式选择；  
b）超速报警情况确认。

表 55 CBTC 车载 ATP 输入数据  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 6.11 自诊断、故障报警及数据记录

ATP 车载设备具备自诊断、故障报警及列车运行重要数据的记录功能，并可通过离线设备打印。记录的内容包括事件的时间和日期，并保存 7 天，保存的数据可实现上传，并宜实现自动转存。记录内容包括：设备运行状况、行车里程、控制情况、驾驶模式、速度、列车日检数据。表 56 规定了自诊断、故障报警及数据记录的内容。

表 56 自诊断、故障报警及数据记录  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td></td></tr></table>

# 7 ATO功能分配

# 7.1 功能描述

ATO主要功能如图11所示

# 7.2 确定ATO曲线

# 7.2.1 为启动、停止、调速，确定ATO曲线

CBTC系统应为列车确定ATO曲线ATO子系统在ATP子系统的保护下，根据ATS子系统的命令，实现对列车的自动驾驶、列车在区间运行的自动调整，并可实现列车的节能运行控制ATO子系统可控制列车按运行图规定的区间走行时分行车，自动完成对列车的启动、加速、巡航、惰行、减速和制动的合理控制。表57规定了ATO曲线的内容。

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/69683818-e6f1-4336-ad86-85967153f544/5a83d7bfe1af3652e6d83ae857f9b8caa3568c5e6a99006faa6b445b1d28b62b.jpg)

表 57 确定 ATO 曲线  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 7.2.2 列车进站精确停车

ATO子系统应具备列车进站精确停车功能，不同编组的列车可以停靠的不同的停车位置。表58规定了列车进站精确停车的内容。

表 58 列车进站精确停车  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 7.3 列车速度调整

# 7.3.1 根据ATO曲线调整列车速度

CBTC系统须根据ATO曲线调整列车速度。表59规定了列车调速的内容。

表 59 列车调速功能  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 7.3.2 跳停

表60规定了ATO响应ATS跳停的内容。

表 60 ATO 响应 ATS 系统设置的跳停命令  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td></td><td>X</td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 7.3.3 运营调整

在AM模式下，ATO子系统可根据ATS的调整指令控制区间走行时分，达到列车运行自动调整的目的。表61规定了列车自动调整的内容。

表 61 列车运行自动调整功能  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td></td><td>X</td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 7.3.4 在线列车监控

ATO子系统向ATS子系统发送列车运行信息，以便ATS子系统能对在线列车进行监控。表62规定了在线列车进行监控的内容。

表 62 在线列车进行监控  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC 轨旁</td><td></td><td>X</td><td>X</td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td></td></tr></table>

# 7.4 门控制

# 7.4.1 开列车门/站台门

表63和表64规定了门控制的内容

# 7.4.1.1 开列车门

在AM驾驶模式下，在ATP的防护下可提供自动开门或者人工开门两种开门方式，见表63。

表63 开列车门  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CI</td><td></td><td></td><td></td></tr><tr><td>车辆(外部接口)</td><td>X</td><td></td><td>X</td></tr></table>

# 7.4.1.2 开站台门

CBTC系统须能自动或者人工开启站台门，见表64。

表64 开站台门  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td>X</td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td></td></tr><tr><td>CI</td><td></td><td></td><td>X</td></tr></table>

# 7.4.2 关列车门/站台门

# 7.4.2.1 概述

表65和表66规定了关列车门/站台门。

# 7.4.2.2 关闭列车门

在AM驾驶模式下，可提供自动关门或者人工关门两种关门方式，见表65和表66。

表 65 关闭列车门  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td>X</td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td></td></tr><tr><td>CI</td><td></td><td></td><td></td></tr><tr><td>车辆(外部接口)</td><td>X</td><td></td><td>X</td></tr></table>

表 66 关闭站台门  

<table><tr><td colspan="4">子功能:关闭站台门CBTC系统应能自动或者人工关闭站台门</td></tr><tr><td colspan="4">功能分配:</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td></td></tr><tr><td>CI</td><td></td><td></td><td>X</td></tr></table>

# 7.5 车载ATO用户界面

在列车显示屏上显示的CBTC车载ATO数据应由授权管理部门规定。表67规定了ATO显示数据的内容。

表 67 CBTC 车载 ATO 显示数据  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td>X</td><td>X</td></tr></table>

# 7.6 自诊断、故障报警及数据记录

# 7.6.1 概述

表68和表69规定了自诊断、故障报警及数据记录的内容。

# 7.6.2 自诊断、故障报警及数据记录

ATO子系统应具有自诊断功能，记录和分析故障报警信息，并能将报警信息传至中心ATS，见表68。

表 68 自诊断、故障报警及数据记录  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td></td></tr></table>

# 7.6.3 车载旅客信息数据

ATO 车载设备应向 TMS 提供有关车载旅客信息的数据，见表 69。

表 69 车载旅客信息数据  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td></td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td>X</td><td>X</td><td></td></tr><tr><td>外部车辆系统</td><td></td><td></td><td>X</td></tr></table>

# 8 ATS功能分配

# 8.1 功能描述

图12总结了主要的与CBTC相关的ATS功能。

# 8.2 列车识别

# 8.2.1 概述

表70和表71规定了列车识别号的内容。

# 8.2.2 CBTC的运行列车识别号

每一个运行在CBTC区域内的装备CBTC的列车都应该分配一个运行列车标识号，列车识别号应由列车表号、车次号、车组号、目的地号组成。见表70。

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/69683818-e6f1-4336-ad86-85967153f544/e0c00fdee8fe0ff209d53aeda36523d933d4bd235fc880020c71ed60664175f0.jpg)  
图12 ATS的主要功能

表 70 CBTC 的运行列车识别号  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td></td><td></td></tr></table>

# 8.2.3 列车识别号丢失处理

在列车识别号因故丢失情况下，系统应根据运行图、列车位置及时间自动推算并自动设置列车识别号，且能通过车-地双向通信传输信息校核，见表71。

表 71 列车识别号丢失处理  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td></td><td></td></tr></table>

# 8.3 列车追踪

ATS系统应该具有自动追踪，获取所有运行在CBTC区域的装备CBTC的列车记录并在ATS用户界面显示位置、标识、列车时刻表，及其他的相关信息并保持这些信息的能力。列车的前后位置应该依据CBTC列车位置报告来进行追踪并显示在ATS用户界面上列车在车辆段/停车场内运行时应具有车组号的跟踪、显示功能。表72规定了ATS列车追踪的内容。

表 72 ATS 列车追踪  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td>X</td><td>X</td></tr><tr><td>CBTC轨旁</td><td>X</td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td></td><td></td></tr><tr><td>CI</td><td></td><td></td><td></td></tr></table>

# 8.4 列车进路办理

# 8.4.1 概述

表73～表75规定了列车进路办理的内容。

# 8.4.2 列车进路办理——自动

ATS系统应该具有列车自动办理进路的功能。ATS系统依照列车运行图/时刻表、在线列车运行信息、车站联锁表自动设置发车进路，指挥在线列车运行，见表73。

表 73 列车进路自动办理  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CBTC轨旁</td><td>X</td><td></td><td>X</td></tr><tr><td>CBTC车载</td><td>X</td><td></td><td></td></tr><tr><td>CI</td><td>X</td><td></td><td>X</td></tr></table>

# 8.4.3 列车人工进路办理

ATS系统应该具有手动办理进路的功能，见表74。

表 74 列车人工进路办理  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CBTC轨旁</td><td></td><td>道交</td><td>X</td></tr><tr><td>CBTC车载</td><td></td><td></td><td></td></tr><tr><td>CI</td><td>X</td><td></td><td>X</td></tr></table>

# 8.4.4 列车进路办理——冲突检查

当列车运行偏离计划，不同运行交路的列车经过同一地点时，系统应能检测到列车计划冲突，并提示调度员采取列车计划冲突干预方案，见表75。

表 75 列车进路冲突检查  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td></td><td></td><td></td></tr><tr><td>CI</td><td></td><td></td><td></td></tr></table>

# 8.5 列车调整

# 8.5.1 列车自动调整

# 8.5.1.1 概述

表76～表78规定了列车调整的内容。

# 8.5.1.2 自动调度

ATS系统可包括自动调度功能，见表76、

表 76 自动调度  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td>X</td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td></td><td></td><td>X</td></tr></table>

# 8.5.1.3 列车时刻表/发车（运行）间隔调整

ATS系统可具有监视与自动调整的功能，见表77。

表 77 列车时刻表调整功能  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td>X</td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td></td><td></td><td>X</td></tr></table>

# 8.5.1.4 冲突自动调整

在CBTC列车位置报告的基础上，ATS系统应包括基于列车位置报告的列车自动调整功能，来处理列车冲突，以把整个系统的延迟减少到最

小，见表78。

表 78 冲突自动调整  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td>X</td><td></td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td></td><td></td><td>X</td></tr><tr><td>CI</td><td></td><td></td><td></td></tr></table>

# 8.5.2 节能运行

ATS系统可具有通过实时控制及协调列车加速、列车滑行、列车制动来实施能源优化的功能。表79规定了节能运行的内容。

表 79 节能运行  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td>X</td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td></td><td>X</td><td>X</td></tr></table>

# 8.6 列车运行控制

# 8.6.1 扣车

ATS系统应具有在车站扣车能力。表80规定了扣车的内容。

表 80 扣车功能  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td></td><td></td><td>X</td></tr><tr><td>CI</td><td></td><td>X</td><td></td></tr></table>

# 8.6.2 提前发车

ATS系统应具有设置站台提前发车的功能。表81规定了提前发车的内容。

表81 提前发车  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td>X</td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td></td><td></td><td>X</td></tr></table>

# 8.6.3 跳停

ATS系统应具有设置一个或多个装备CBTC的列车经过下一个或下几个车站而不停车的功能。表82规定了跳停车站的内容。

表82 跳停车站  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td>X</td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td></td><td></td><td>X</td></tr></table>

# 8.6.4 控制权转换

在紧急情况下，车站值班员可在控制工作站上强行取得控制权，控制车站的进路和信号列车进路控制权的优先级为本地控制优先于中央控制；在本地控制或中央控制时，人工控制优先于自动控制。表83规定了控制权转换的内容。

表 83 控制权转换  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td></td><td></td><td></td></tr><tr><td>CI</td><td>X</td><td>X</td><td>X</td></tr></table>

# 8.7 控制列车运行

ATS系统应具有在CBTC区域内任何轨道区段，设置（与取消）临时限速的能力。表84规定了临时限速的内容。

表84 临时限速  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td>X</td><td></td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td>X</td></tr><tr><td>CBTC 车载</td><td></td><td></td><td>X</td></tr></table>

# 8.8 时刻表编制

ATS应具备变更计划运行图/时刻表的功能，并按照变更后的结果组织和实施当日的列车运行。表85规定了时刻表编制的内容。

表 85 时刻表编制  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td></td><td></td><td></td></tr></table>

# 8.9 模拟培训

ATS应具备模拟演示及培训系统，实现对调度员的培训。表86规定了模拟培训的内容。

表 86 模拟培训  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td></td><td></td><td></td></tr></table>

# 8.10 用户界面

# 8.10.1 显示数据

CBTC的ATS显示应能表示以下信息：

a）精确的和区域相关的信息；  
b）列车状态相关信息；  
c） 列车移动授权/进路信息；  
d）被控列车运行相关的信息，如防护区段信息、锁闭的进路/区段以及临时限速极限和限速值；  
e）其他。

表87规定了ATS显示数据的内容。

表 87 ATS 显示数据  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CBTC 轨旁</td><td>X</td><td></td><td></td></tr><tr><td>CBTC 车载</td><td>X</td><td></td><td></td></tr><tr><td>CI</td><td>X</td><td></td><td></td></tr></table>

# 8.10.2 数据管理

# 8.10.2.1 概述

表 88 ~ 表 90 规定了 CBTC 输入数据的内容。

# 8.10.2.2 CBTC输入数据

CBTC的ATS用户界面显示应能够接收以下ATS用户输入：

a）办理和取消进路输入；  
b）建立和取消防护区段，锁闭进路/区段，以及临时限速输入；  
c） 其他。

表88规定了CBTC输入数据的内容。

表 88 CBTC 输入数据  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td></td><td></td><td></td></tr></table>

# 8.10.2.3 发送报警数据

ATS子系统可将自身的报警信息、ATP车载子系统、ATO子系统、CI子系统的报警信息传至控制中心维护工作站、车站维护工作站、综合维修中心的信号监测报警工作站，见表89。

表 89 发送报警数据  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td>X</td><td></td></tr><tr><td>CBTC轨旁</td><td>X</td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td></td><td></td></tr><tr><td>CI</td><td>X</td><td></td><td></td></tr><tr><td>MSS</td><td></td><td></td><td>X</td></tr></table>

# 8.10.2.4 数据记录及回放

系统应对各种操作信息、设备运行状态信息及运行数据进行记录和备份，并具有根据记录数据对任何时间、任何信息点进行过程回放功能，综合维修中心的信号监测报警工作站系统应具备在线回放功能，回放记

录应保存不少于30天，见表90。

表 90 数据记录及回放  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td>X</td><td>X</td></tr><tr><td>CBTC轨旁</td><td>X</td><td></td><td></td></tr><tr><td>CBTC车载</td><td>X</td><td></td><td></td></tr><tr><td>CI</td><td>X</td><td></td><td></td></tr><tr><td>MSS</td><td></td><td></td><td>X</td></tr></table>

# 9 CI功能分配

# 9.1 功能描述

CBTC相关的CI主要功能分配，如图13所示。

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/69683818-e6f1-4336-ad86-85967153f544/3499b2fc95269b8a5a041d29b729ad768b678600149892ecb5a2b608f37f2b69.jpg)  
图13 CI的主要功能

# 9.2 进路办理

# 9.2.1 功能描述

表  $91\sim$  表93规定了进路办理的内容。

# 9.2.2 进路办理

联锁应具备进路办理功能。包括人工办理列车进路、设置自动进路和自动折返进路。联锁将办理的进路信息提供给ATP系统，用于移动授权的计算，见表91。

表 91 进路办理  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td>X</td></tr><tr><td>CBTC车载</td><td></td><td></td><td></td></tr><tr><td>CI</td><td>X</td><td>X</td><td></td></tr></table>

# 9.2.3 装有无效CBTC装备的列车进路办理

对于设备故障的CBTC列车或无装备的列车，在前方进路出清并重新开放后，装有无效CBTC装备的列车方可驶入，见表92。

表 92 故障列车进路办理  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC车载</td><td></td><td></td><td></td></tr><tr><td>CI</td><td>X</td><td>X</td><td>X</td></tr></table>

# 9.2.4 保护区段

联锁子系统除对正常的列车进路进行防护外，还应建立列车进路的保护区段，并予以防护，见表93。

表 93 保护区段  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td></td><td></td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td>X</td></tr><tr><td>CBTC车载</td><td></td><td></td><td></td></tr><tr><td>CI</td><td>X</td><td>X</td><td></td></tr></table>

# 9.3 锁闭/解锁进路/区段

# 9.3.1 概述

表 94 ~ 表 97 规定了锁闭/解锁进路/区段的内容。

# 9.3.2 进路/区段锁闭

系统应具有锁闭（并随后解锁）CBTC区域内的道岔、信号机或轨道区段的能力，CI子系统应对进路实现预先锁闭和接近锁闭，锁闭的进路随列车的运行自动分段解锁，见表94。

表 94 进路/区段锁闭  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td></td><td>X</td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td>X</td></tr><tr><td>CBTC 车载</td><td></td><td></td><td></td></tr><tr><td>CI</td><td>X</td><td>X</td><td></td></tr></table>

# 9.3.3 道岔单操、单锁

联锁应具备道岔单独操纵及锁闭的能力，见表95。

表 95 道岔操作  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td></td><td>X</td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td>X</td></tr><tr><td>CBTC车载</td><td></td><td></td><td></td></tr><tr><td>CI</td><td>X</td><td>X</td><td></td></tr></table>

# 9.3.4 计轴故障恢复

系统应具有计轴故障恢复的能力，见表96。

表 96 计轴故障恢复  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td>X</td><td></td><td>X</td></tr><tr><td>CBTC 轨旁</td><td></td><td></td><td>X</td></tr><tr><td>CBTC 车载</td><td></td><td></td><td></td></tr><tr><td>CI</td><td>X</td><td>X</td><td></td></tr></table>

# 9.4 紧急停车按钮

联锁子系统检查站台紧急停车按钮的状态，一旦检测到按钮被按下，应立即关闭相应的进路。表97规定了紧急停车按钮的内容。

表 97 紧急停车按钮  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC轨旁</td><td></td><td>X</td><td>X</td></tr><tr><td>CBTC车载</td><td></td><td></td><td></td></tr><tr><td>CI</td><td>X</td><td>X</td><td></td></tr></table>

# 9.5 故障监测及操作记录

CI子系统具有自检、自诊断和对信号机、转辙机等基础信号设备的监测报警功能，并在车站的维护工作站上显示及报警。表98规定了故障监测及操作记录的内容。

表 98 故障检测  

<table><tr><td>功能分配</td><td>输入</td><td>实现</td><td>输出</td></tr><tr><td>ATS</td><td></td><td></td><td>X</td></tr><tr><td>CBTC轨旁</td><td></td><td></td><td></td></tr><tr><td>CBTC 车载</td><td></td><td></td><td></td></tr><tr><td>CI</td><td>X</td><td>X</td><td>X</td></tr></table>

# 参考文献

[1] IEEE 1474.3 IEEE Recommended Practice for Communications-Based Train Control (CBTC) System Design and Functional Allocations

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/69683818-e6f1-4336-ad86-85967153f544/193928de56568f622e5aef60a5a43c61600659a97a9f892d132b8a3641faefcf.jpg)

中国城市轨道交通协会团体标准

城市轨道交通 基于通信的列车运行

控制系统（CBTC）互联互通系统规范

第2部分：系统架构和功能分配

T/CAMET 04010.2-2018

※

中国铁道出版社有限公司出版发行

（100054，北京市西城区石安门西街8号）

公司网址：http://www.tdpress.com

北京铭成印刷有限公司印刷

开木：  $880\mathrm{mm}\times 1230\mathrm{mm}$  1/32印张：2.25 字数：61千

2019年5月第1版 2019年5月第1次印刷

书号：15113·5656

定价：20.00元

版权所有 侵权必究

凡购买铁道版图书，如有印制质量问题，请与本公司发行部联系调换。

发行部电话：路（021）73174，市（010）51873174