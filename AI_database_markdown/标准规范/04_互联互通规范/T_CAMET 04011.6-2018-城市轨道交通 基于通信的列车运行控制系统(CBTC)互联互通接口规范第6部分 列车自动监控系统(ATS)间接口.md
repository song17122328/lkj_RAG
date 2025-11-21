# 中国城市轨道交通协会团体标准

T/CAMET 04011.6—2018

# 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范第6部分：列车自动监控系统（ATS）间接口

Urban rail transit — Interface specification for interoperability of communication based train control system

Part 6: Interface between automatic train supervision systems

2018-09-10 发布

2018-12-31 实施

# 目次

前言 V  
引言 VIII

1 范围 1  
2 规范性引用文件 1  
3 术语和缩略语 2

3.1 术语  
3.2 缩略语 3

4总则 4  
5 ATS-ATS报文规范 4

5.1 通信机制  
5.2 接口详细描述 5

附录A（规范性附录） 设备类型定义、设备色码定义、列车信息识别号字段说明 25

# 前言

T/CAMET04011《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范》分为以下八个部分：

——第1部分：应答器报文；  
第2部分：CBTC系统车地连续通信协议；  
——第3部分：车载列车自动保护（ATP）/列车自动运行（ATO）系统与车辆的接口；  
- 第4部分：区域控制器（ZC）间接口；  
-第5部分：计算机联锁（CI）间接口；  
- 第6部分：列车自动监控系统(ATS)间接口；  
- 第7部分：信号各子系统与维护支持系统(MSS)间接口；  
——第8部分：车载人机界面。

本部分是T/CAMET04011的第6部分。

本部分按照GB/T1.1—2009给出的规则起草。

请注意本部分的某些内容可能涉及专利，本部分的发布机构不承担识别这些专利的责任。

本部分由中国城市轨道交通协会技术装备专业委员会提出。

本部分由中国城市轨道交通协会归口。

本部分起草单位：北京全路通信信号研究设计院集团有限公司、交控科技股份有限公司、中国铁道科学研究院集团有限公司通信信号研究所、株洲中车时代电气股份有限公司、浙江众合科技股份有限公司。

本部分主要起草人：编写组：陈逸、肖孟、李弘、郭辉、宋丽丽、张德明、郭戩、王丽丽、黎邓根、邬斌剑、王春。审核组：李中浩、朱翔、赵炜、郑生全、张艳兵、张良、王道敏、张琼燕、段晨宁、李新文、李德堂、文成祥、任敬、朱东飞、肖利君、张守芝、刘新平。

# 引言

为促进中国城市轨道交通建设，实现并满足城市轨道交通互联互通的需要，达到经济适用、资源共享、技术先进及可持续发展的目标，制定城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系列团体标准。

该系列规范包括《城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通系统规范》《城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通接口规范》《城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通测试规范》《城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通工程规范》4个规范(17个部分)。

# 城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通接口规范第6部分：列车自动监控系统(ATS)间接口

# 1 范围

T/CAMET04011的本部分规定了互联互通相邻线路间线路级列车自动监控系统（以下简称ATS）的接口，主要包括通信架构、信息内容、数据交互流程、可扩展性、设备类型定义、设备色码定义、列车信息识别号字段说明。

本部分适用于国内采用基于通信的列车运行控制系统（CBTC）的新建、更新改造及扩建的城市轨道交通线路建设，用于指导信号系统的系统设计、产品设计、设备招标、工程建设。

# 2 规范性引用文件

下列文件对于本部分的应用是必不可少的。凡是注日期的引用文件，仅所注日期的版本适用于本部分。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本部分。

CJ/T407—2012城市轨道交通基于通信的列车自动控制系统技术要求

T/CAMET04010.1—2018城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系统规范第1部分：系统总体要求

运基信号[2010]267号 RSSP - I 铁路信号安全通信协议

IEEE802.3 以太网（Ethernet）

RFC791 互联网协议(InternetProtocol)

RFC793 传输控制协议（TransmissionControlProtocol）

# 3 术语和缩略语

GB50157—2013、CJ/T407—2012和T/CAMET04010.1—2018界定的及下列术语和缩略语适用于本部分。为了便于使用，以下重复列出了其中的主要相关术语。

# 3.1 术语

3.1.1

基于通信的列车控制 communication based train control (CBTC)

通过不依赖轨旁列车占用检测设备的列车主动定位技术、连续车-地双向数据通信技术以及能够执行安全功能的车载和地面处理器而构建的连续式列车自动控制系统。

[CJ/T407—2012，定义3.1.1]

3.1.2

正线 main line

载客列车运营的贯穿全程的线路。

[GB50157—2013，定义2.0.11]

3.1.3

列车自动监控 automatic train supervision

根据列车时刻表为列车运行自动设定进路、指挥行车、实施列车运行管理等技术的总称。

[GB50157—2013，定义2.0.38]

3.1.4

列车自动防护 automatic train protection

自动实现列车运行间隔、超速防护、进路安全和车门等监控技术的总称。

[GB50157—2013，定义2.0.39]

3.1.5

列车自动运行 automatic train operation

自动实现列车加速、调速、停车和车门开闭、提示等控制技术的总称。

[GB50157—2013，定义2.0.40]

3.1.6

# 计算机联锁 computer interlocking

以计算机技术为核心，自动实现进路、道岔、信号机等防护技术的总称。

[CJ/T407—2012，定义3.1.6]

3.1.7

# 移动授权 movement authority

列车沿给定的行驶方向进入并在某一特定轨道区段内行车的许可。

[CJ/T407—2012，定义3.1.7]

3.1.8

# 转换轨 transfer track

指车辆段/停车场与正线的连接轨，运营列车在驶入/驶出转换轨过程中，当条件具备时，进行列车运行控制级别及驾驶模式转换。

[T/CAMET 04010.1,术语3.1.13]

3.1.9

# 跨线运行 overline operation

运营列车在两条或两条以上制式相同或兼容的线路中，由一条线路进入另外一条线路进行共线运行的方式。

[T/CAMET 04010.1—2018,术语3.1.14]

3.1.10

# 互联互通 interoperability

装备不同信号厂家车载设备的列车可以在装备不同信号厂家轨旁设备的一条轨道交通线路内或多条轨道交通线路上无缝互通安全可靠运营。

[T/CAMET 04010.1—2018,术语3.1.16]

# 3.2 缩略语

AM：列车自动驾驶模式（Automatic Train Operating Mode）

ATO：列车自动运行（Automatic Train Operation）

ATP：列车自动防护（Automatic Train Protection）

ATS：列车自动监控（Automatic Train Supervision）

CBTC：基于通信的列车控制（Communication Based Train Control）

CI:计算机联锁（Computer Interlocking）

CM：列车自动防护模式（Coded Train Operating Mode）

EUM: 非限制人工驾驶模式 (Emergency Unrestricted Train Operating Mode)

GAL：通用应用层（Generic Application Layer）

IPv4：互联网协议(Internet Protocol，IP)的第4版

MA: 移动授权 (Movement Authority)

PSD：站台门（Platform Screen Door）

RM：限制人工驾驶模式（Restricted Train Operating Mode）

TCP：传输控制协议（Transmission Control Protocol）

TSR：临时限速（Temporary Speed Restriction）

ZC：区域控制器（ZoneController）

# 4 总则

城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通的一个重要目标是可实现列车跨线路运行，列车跨线运行涉及到不同厂商、多条线路的ATS之间在列车运行调度指挥方面进行协调、交接。当前ATS接口支撑的功能包括：互联互通线路站场信息共享、跨线运行列车信息共享、跨线运行列车计划调整信息共享、跨线运行列车接入站首站跳停命令下达功能。根据后续工程实施中用户需求的增加，可对ATS间接口内容进行扩展。

# 5 ATS-ATS报文规范

# 5.1 通信机制

ATS间通信机制如下：

a）相邻ATS间通信应采用周期与非周期发送的方式进行通信；  
b）通信双方应均采用大端字节序进行数据传输。

# 5.2 接口详细描述

# 5.2.1 通信层次结构描述

ATS间通信层次结构划分见图1。

图1 ATS间通信层次结构  
![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/fba1dfbd-f13c-49cc-a45a-45428eef4ff4/ef5338f30fa41f378d8f7600280a3b1b47c98e4857f091f11974459d0f85fd77.jpg)  
注：物理层：采用 IEEE802.3 标准协议  
数据链路层：采用IEEE802.3标准协议  
网络层：IPv4。  
传输层：TCP协议。  
应用层：参见5.2.3详细定义。

# 5.2.2 接口连接方式

# 5.2.2.1 物理接口

ATS应冗余接入通信网络，网络拓扑结构为A网-A网、B网-B网，接口间宜通过防火墙进行隔离。

# 5.2.2.2 通信层次描述

ATS与ATS间应建立对等的逻辑连接。通信层次如图2所示（箭头

指向表示服务端，红蓝线表示双网逻辑连接）。

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/fba1dfbd-f13c-49cc-a45a-45428eef4ff4/b0d0e2cd0e044dc3a186f915e1a24954c2a555ae7868ba1f6ea07f434369caa0.jpg)  
第一组通道

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/fba1dfbd-f13c-49cc-a45a-45428eef4ff4/1c12be5e37b92bc20f77230ac87543321be955945040af5be32c828ead112d11.jpg)  
第二组通道

说明：

第一组通道，线路一ATS的主机应作为客户端同时与线路二ATS的主机和备机建立双网连接，用于传送本线路内产生的信息。

第二组通道，线路二ATS的主机应作为客户端同时与线路一ATS的主机和备机建立双网连接，用于传送本线路内产生的信息。

服务端侦听端口应为9900。

# 5.2.2.3 动态交互描述

# 5.2.2.3.1 信息帧格式定义

相邻ATS间每个周期需要交互的信息应组成通用应用层（GAL）信息包进行传输，如图3所示。

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/fba1dfbd-f13c-49cc-a45a-45428eef4ff4/fdc15a3d50ccd3877c17e85c8fb8d8ccc905935f02e5f05b17cb561d459e3768.jpg)  
图2 通信层次  
图3 GAL信息包和应用层信息包关系结构图

# 5.2.2.3.2 信息包格式定义

ATS间通信的GAL信息包中包含ATS间传输的各条应用信息。每

个GAL信息包总长应不得超过65000字节。每个GAL信息包应只包含一类应用信息包。GAL信息包格式定义见表1和表2。

表 1 GAL 信息包格式定义  

<table><tr><td>信息域定义</td><td>字节编号</td><td>字段</td><td>长度</td><td>信息位定义及说明</td></tr><tr><td rowspan="2">帧头</td><td>1</td><td rowspan="2"></td><td rowspan="2">2字节</td><td rowspan="2">0xEFDFD</td></tr><tr><td>2</td></tr><tr><td rowspan="8">双网序列号</td><td>3</td><td rowspan="8"></td><td rowspan="8">8字节</td><td rowspan="8">用于将GAL包双网传输的唯一标识。发送方设置,双网发送数据时,同一GAL包的双网序列号必须保证相同。通信连接建立后,通信双方将各自的“双网序列号”置0,并随着GAL包的发送递增计数,每发一包,计数加1,到达8字节限制后又变成0。接收方接收双网数据时,如果当前GAL包的双网序列号等于或小于上一个接收的GAL包的双网序列号,则丢弃当前GAL包</td></tr><tr><td>4</td></tr><tr><td>5</td></tr><tr><td>6</td></tr><tr><td>7</td></tr><tr><td>8</td></tr><tr><td>9</td></tr><tr><td>10</td></tr><tr><td rowspan="2">接口信息类型</td><td>11</td><td>类型高位</td><td rowspan="2">2字节</td><td rowspan="2">0xEF0404:ATS-ATS接口</td></tr><tr><td>12</td><td>类型低位</td></tr><tr><td rowspan="4">发送方标识信息</td><td>13</td><td rowspan="4">源ID</td><td rowspan="4">4字节</td><td rowspan="4">发送方设备ID</td></tr><tr><td>14</td></tr><tr><td>15</td></tr><tr><td>16</td></tr><tr><td rowspan="4">接收方标识信息</td><td>17</td><td rowspan="4">目的ID</td><td rowspan="4">4字节</td><td rowspan="4">接收方设备ID</td></tr><tr><td>18</td></tr><tr><td>19</td></tr><tr><td>20</td></tr><tr><td rowspan="4">数据版本校验信息</td><td>21</td><td rowspan="4">数据版本</td><td rowspan="4">4字节</td><td rowspan="4">ATS重叠区内数据版本信息</td></tr><tr><td colspan="1">22</td></tr><tr><td colspan="1">23</td></tr><tr><td colspan="1">24</td></tr><tr><td rowspan="4">本方消息序列号a</td><td>25</td><td rowspan="4">序列号</td><td rowspan="4">4字节</td><td rowspan="4">记录发送本条消息时,本方的周期计数</td></tr><tr><td colspan="1">26</td></tr><tr><td colspan="1">27</td></tr><tr><td colspan="1">28</td></tr><tr><td rowspan="2">通信周期</td><td>29</td><td rowspan="2">通信周期</td><td rowspan="2">2字节</td><td rowspan="2">设备通信周期,单位:ms</td></tr><tr><td colspan="1">30</td></tr><tr><td>对方消息序列号a</td><td>31</td><td>序列号</td><td>4字节</td><td>记录收到对方上一条消息中的对方消息序列号b</td></tr><tr><td>收到上一条消息时本方序列号a</td><td>32</td><td>序列号</td><td>4字节</td><td>记录收到对方上一条消息时,本方的周期计数b</td></tr><tr><td>协议版本号c</td><td>33</td><td>协议版本号</td><td>1字节</td><td>ATS-ATS的协议版本,可参照工程约定</td></tr><tr><td>应用层信息包个数</td><td>34</td><td>应用层信息包个数</td><td>1字节</td><td>GAL包内含有的所有应用层信息包个数</td></tr><tr><td rowspan="2">应用层信息长度</td><td>35</td><td rowspan="2">应用层信息长度</td><td rowspan="2">2字节</td><td rowspan="2">“应用层信息”的长度,单位:字节</td></tr><tr><td colspan="1">36</td></tr><tr><td>应用层信息</td><td></td><td>应用层信息</td><td>变长</td><td>参见表2格式定义</td></tr><tr><td>帧尾</td><td></td><td></td><td>2字节</td><td>0xFDFD</td></tr><tr><td colspan="5">a序列号有效值为1~(231-1)。发送方应保证生成两包信息包时,两包信息报中的“本方消息序列号”字段的差值与“通信周期”相乘等于生成两包消息的时间间隔,主要用于心跳信息包交互时判断通信延时的参考依据,但不强制要求通信延时的处理方式。b当未收到对方消息时,此字段应填写0xFFFFFFFF。cATS判断“协议版本号”字段校验不通过时,应进行丢包或断开通信处理。</td></tr></table>

表 2 应用层信息格式定义  

<table><tr><td>信息域定义</td><td>字节编号</td><td>报文内容</td><td>说 明</td></tr><tr><td rowspan="2">报文长度</td><td>1</td><td rowspan="2">报文长度(报文类型~报文结束)</td><td rowspan="2">自定义,详细内容参见5.2.3.1</td></tr><tr><td>2</td></tr><tr><td rowspan="2">报文类型</td><td>3</td><td rowspan="2">定义某一条应用信息的标识</td><td rowspan="2">自定义,详细内容参见5.2.3.1</td></tr><tr><td>4</td></tr><tr><td rowspan="2">总包数</td><td>5</td><td rowspan="2">总的要发送的信息包的数量道</td><td rowspan="2">应用层信息包需要拆分时,拆分后的信息包数量</td></tr><tr><td>6</td></tr><tr><td rowspan="2">当前包号</td><td>7</td><td rowspan="2">正在发送的信息包序号,从1开始</td><td rowspan="2">应用层信息包需要拆分时,此信息包在所有信息包中的序号</td></tr><tr><td>8</td></tr><tr><td>报文内容</td><td>9~报文结束</td><td>按照报文格式定义的报文具体内容</td><td>自定义,详细内容参见5.2.3.3</td></tr></table>

# 5.2.2.3.3 通信状态的监督和管理

ATS间通信状态的监督和管理如下：

a）ATS应对接收到的应用信息进行合法性检查。若检查未通过，应认为本周期未收到相邻ATS的应用信息，并应记录报警信息。具体检查方式如下：

1）信息内容的一致性检查：包括信息的字段合法性检查、字段组合合法性检查、以及信息完整性检查；  
2）GAL信息包数据所应包含的信息的完整性；  
3）其他逻辑检查。

b）ATS应能对通信连接状态进行判断，即应用层根据GAL信息包头中字段进行判断：

1）ATS与相邻ATS通信中断的超时时间值（  $T_{\mathrm{ATSTimeout}}$  ）应可配置（范围：  $3\mathrm{s}\sim 9\mathrm{s}$  )，且宜采用推荐值：6s。  
2）若ATS在  $T_{\mathrm{ATSTInout}}$  超时时间内，没有接收到来自相邻ATS的任何消息，则ATS应认为与相邻ATS通信中断。若ATS收到双网的通信通道中的任何一网通道上的正确数据，即应认为该通信连接恢复。  
3）若ATS判断接收到相邻ATS的周期性应用信息延迟已经达到或超过  $T_{\mathrm{ATSTimout}}$  时，ATS可丢弃此信息包，并应认为与相邻ATS通信中断或发生丢包。  
4）通信中断的情况下，应生成报警信息。  
5）连接断开时应立即重连。  
6）互联互通线网中，各厂商的ATS间的通信超时时间应一致，消息有效期时间应一致。

c）通信中断的倒机切换逻辑：

1）ATS和相邻ATS的备机只有在完成了与各自系统主机的同步，真正进入备机状态以后才应与对方进行通信联系。  
2）ATS和相邻ATS在通信中断后应首先尝试重新建立连接，只有在重建连接仍不成功后，才应进行倒机切换逻辑判断。  
3）ATS主备机之间、相邻ATS主备机之间应通过其他的物理连接相互沟通各自系统主备机之间的通信连接状态，为倒机切换提供准确、可靠的判断依据。  
4）ATS和相邻ATS只有在主机之间的通信连接发生故障以

后才应进行倒机切换。备机与备机之间、主机与备机之间的通信中断后只报警而不倒机。

5）ATS和相邻ATS主机通信中断且持续一段时间（该时间应可配置，范围：  $2\mathrm{s}\sim 4\mathrm{s})$  内不能恢复，且在判断ATS备机与相邻ATS主机通信正常的情况下，ATS才应进行倒机切换。

# 5.2.3 接口数据描述

# 5.2.3.1 数据类型定义

表3规定了ATS间通信的所有应用信息类型及其含义、发送方向、长度范围、发送方式（周期/非周期）的内容。

表 3 ATS 间通信的应用层信息定义  

<table><tr><td>信息类型</td><td>信息包名</td><td>发送方向</td><td>长度(至少字节数)</td><td>发送方式</td></tr><tr><td>0x0201</td><td>站场显示信息包</td><td>双向</td><td>4</td><td>周期</td></tr><tr><td>0x0202</td><td>列车信息包</td><td>双向</td><td>4</td><td>周期</td></tr><tr><td>0x0203</td><td>列车运行调整信息包</td><td>交出站→接入站</td><td>4</td><td>周期</td></tr><tr><td>0x0204</td><td>列车接入站跳停命令信息包</td><td>接入站→交出站</td><td>4</td><td>非周期</td></tr><tr><td>0x0205</td><td>列车接入站跳停回执信息包</td><td>交出站→接入站</td><td>4</td><td>非周期</td></tr><tr><td>0x020A</td><td>ATS城市自定义信息包</td><td>双向</td><td>4</td><td>非周期</td></tr><tr><td>0x020B</td><td>ATS厂商自定义信息包</td><td>双向</td><td>4</td><td>非周期</td></tr></table>

# 5.2.3.2 数据交互方式定义

图4表明了两个线路ATS间互传的数据流，具体定义如下：

a）A：本线路的列车运行调整信息；  
b）B：本线路的站场显示信息、列车信息、接入站跳停命令及回执信息；  
c）C：心跳信息。

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/fba1dfbd-f13c-49cc-a45a-45428eef4ff4/70381fbb3e542cdda4184b9d4545c6959e69bb8a55caff3f3fad98558288d2a7.jpg)  
图4 数据交互方式

说明：

箭头方向表示数据流向，实线表示通信连接建立且发送数据，虚线表示通信连接建立但只发送心跳信息，不发送其他信息。

# 5.2.3.3 应用信息定义

# 5.2.3.3.1 说明

本节中的“无效”值：正常通信时发送方不可能发送的非法取值。接

收方收到GAL包中的应用信息包中存在“无效”值时，应对GAL包应用信息包中无效字段进行容错处理。

本节中的“默认”值：

a)针对具体工程中不实现的功能，通信双方可在具体工程中约定，相关字段取值应按照“默认”值发送。  
b) 设备在初始化完成前, 无法确定状态时, 相关字段取值应按照“默认”值发送。接收方收到“默认”值后, 应认为信息有效, 不进行处理。

本节中涉及“上行”、“下行”的方向定义，应采用运营方向规定的上下行。

# 5.2.3.3.2 心跳信息包

ATS应周期性发送心跳信息，具体格式同应用信息包为0的GAL信息包。

# 5.2.3.3.3 站场显示信息包

ATS应周期性将复视车站的所有站场显示信息发送给相邻ATS，见表4。

表 4 站场显示信息包  

<table><tr><td colspan="3">字 段</td><td>长度/字节</td><td>说 明</td></tr><tr><td colspan="3">线路号</td><td>4</td><td>轨线路ID</td></tr><tr><td colspan="3">时间</td><td>9</td><td>本信息包产生时间。以数字表示年(2字节)、月、日、时、分、秒、毫秒(2字节)</td></tr><tr><td colspan="3">车站信息个数</td><td>1</td><td>信息包内车站个数</td></tr><tr><td rowspan="4">车站信息1</td><td colspan="2">站码</td><td>4</td><td>车站ID</td></tr><tr><td colspan="2">站信息长</td><td>2</td><td>站信息字节长度</td></tr><tr><td rowspan="2">设备信息1</td><td>设备类型</td><td>1</td><td>数值,取值见附录A.1。其他值无效</td></tr><tr><td>设备编号</td><td>4</td><td>每站每种设备类型下单独编号,设备类型和设备编号一起应能唯一标识一个站内的设备。设备编号应优先采用互联互通号系统</td></tr><tr><td rowspan="6">车站信息1</td><td rowspan="3">设备信息1</td><td>设备编号</td><td>4</td><td>设备编号。当互联互通信号系统设备编号文件未规定该设备的编号时,可由信息发送方厂家自行配置</td></tr><tr><td>色码长度</td><td>1</td><td colspan="1">数值,表示色码字节个数</td></tr><tr><td>色码</td><td>N</td><td colspan="1">N个字节顺序组成(bit0~bit8N-1)这8N个bit位。色码意为设备状态组位码,假设设备有n种(n≤8N)独立状态,第i(0≤i&lt;8N)种状态占用Mi位,这Mi位叫做第i个组位,则色码的8N位由这些状态组位组成,设备状态的扩展即为扩组位。色码定义见附录A.2</td></tr><tr><td colspan="2">设备信息2</td><td></td><td colspan="1"></td></tr><tr><td colspan="2">......</td><td></td><td colspan="1"></td></tr><tr><td colspan="2">设备信息n</td><td></td><td colspan="1"></td></tr><tr><td colspan="3">车站信息2</td><td></td><td></td></tr><tr><td colspan="3">......</td><td></td><td></td></tr><tr><td colspan="3">车站信息m</td><td></td><td>m为“车站信息个数”字段取值</td></tr></table>

# 5.2.3.3.4 列车信息包

ATS应周期性将复视车站的所有列车状态信息发送给相邻ATS，见表5。

表 5 列车信息包  

<table><tr><td colspan="3">字 段</td><td>长度</td><td>说 明</td></tr><tr><td colspan="3">线路号</td><td>4</td><td>线路 ID</td></tr><tr><td colspan="3">时间</td><td>9</td><td>本信息包产生时间。以数字表示年(2 字节)、月、日、时、分、秒、毫秒(2 字节)</td></tr><tr><td colspan="3">字 段</td><td>长度</td><td>说 明</td></tr><tr><td colspan="3">车站信息个数</td><td>1</td><td>信息包内车站个数</td></tr><tr><td rowspan="16">车站信息1</td><td colspan="2">站码</td><td>4</td><td>车站ID</td></tr><tr><td colspan="2">列车数量</td><td>2</td><td>车站管辖范围内列车数量</td></tr><tr><td rowspan="14">列车信息1</td><td>列车信息长度</td><td>2</td><td>列车信息字节长度</td></tr><tr><td>源线路号</td><td>4</td><td>详见附录A.3</td></tr><tr><td>目的线路号</td><td>4</td><td>详见附录A.3</td></tr><tr><td>列车类型</td><td>1</td><td>1为计划车,2为头码车,3为人工车,其他无效</td></tr><tr><td>表号长度</td><td>1</td><td>数值</td></tr><tr><td>表号</td><td></td><td>字符,个数由表长度指定,详见附录A.3</td></tr><tr><td>车次号长度</td><td>1</td><td>数值</td></tr><tr><td>车次号</td><td></td><td>字符,个数由车次号长度指定,详见附录A.3</td></tr><tr><td>车组所属线路号</td><td>4</td><td>详见附录A.3</td></tr><tr><td>车组号长度</td><td>1</td><td>数值,详见附录A.3</td></tr><tr><td>车组号</td><td></td><td>字符,个数由车组号长度指定,详见附录A.3</td></tr><tr><td>目的地号长度</td><td>1</td><td>数值</td></tr><tr><td>目的地号</td><td></td><td>字符,个数由目的地号长度指定,详见附录A.3</td></tr><tr><td>最大车头所在逻辑区段编号</td><td>4</td><td>车头所在位置默认值:0xFFFFFFF;无效值:0xFFFFFF</td></tr><tr><td rowspan="9">车站信息1</td><td rowspan="9">列车信息1</td><td>最大车头所在逻辑区段内偏移量</td><td>4</td><td>单位:cm默认值:0xFFFFFF;有效范围:0x0~0xFFFFFFFE</td></tr><tr><td>最小车头所在逻辑区段编号</td><td>4</td><td colspan="1">车尾所在位置默认值:0x00000000;无效值:0xFFFFFFFE</td></tr><tr><td>最小车头所在逻辑区段内偏移量</td><td>4</td><td colspan="1">单位:cm默认值:0xFFFFFFFE;有效范围:0x0~0xFFFFFFFE</td></tr><tr><td>运行方向</td><td>1</td><td colspan="1">ATS系统内的列车运营方向0x01:下行;0x02:上行;0x00:未知;其他无效</td></tr><tr><td>车载ATP报告方向</td><td>1</td><td colspan="1">ATP系统位置报告中的列车方向0x01:下行;0x02:上行;0x00:未知;其他无效</td></tr><tr><td>车轮转向</td><td>1</td><td colspan="1">车轮正转(前进):0x01;车轮反转(后退):0x02;其他值无效。车轮不转动时按正转发送</td></tr><tr><td>早晚点标志</td><td>1</td><td colspan="1">0为正点,1为早点,2为晚点,其他无效</td></tr><tr><td>早晚点时间</td><td>4</td><td colspan="1">数值,单位:s</td></tr><tr><td>列车通信状态</td><td>1</td><td colspan="1">高1bit位1表示ATP切除,0表示ATP未切除,低7bit表示列车状态,1为通信车,2为非通信车,3为通信状态未知,其他无效。补充说明:若某一方ATS无ATP切除功能,则对方作为信息接收方可不处理本字段高1bit,本方作为信息发送方应将本字段高1bit置为0</td></tr><tr><td rowspan="9">车站信息1</td><td rowspan="9">列车信息1</td><td>列车状态</td><td>1</td><td>0x01:CBTC车;0x02:非CBTC车;其他无效</td></tr><tr><td>停准停稳</td><td>1</td><td colspan="1">1:停准且停稳;2:未停准或未停稳;其他无效</td></tr><tr><td>列车速度信息</td><td>2</td><td colspan="1">数值,单位:cm/s默认值:0xFFFF</td></tr><tr><td>车门关闭状态</td><td>1</td><td colspan="1">0x00:开;0x01:关;0xFF:门旁路;其他无效。如无旁路状态应按照关门处理</td></tr><tr><td>ATP系统模式</td><td>1</td><td colspan="1">0x01:RM(限制人工驾驶模式);0x02:CM(列车自动防护模式);0x03:AM(列车自动运行模式);0x04:EUM;0xFF:默认值;其他无效</td></tr><tr><td>ATO工作模式</td><td>1</td><td colspan="1">0x00:ATO未建立;0x03:AM自动驾驶;其他无效</td></tr><tr><td>区间运行调整命令</td><td>2</td><td colspan="1">运行等级或区间运行时间(列车从前一站发车到下一站停车时间,单位:s),可根据工程需求确定</td></tr><tr><td>跳停命令</td><td>1</td><td colspan="1">0x55:有;0xAA:无;0xFF:状态无意义;其他无效</td></tr><tr><td>扣车命令</td><td>1</td><td colspan="1">0x55:有;0xAA:无;0xFF:状态无意义;其他无效</td></tr><tr><td rowspan="6">车站信息1</td><td rowspan="4">列车信息1</td><td>列车阻塞a</td><td>1</td><td>0x01:列车阻塞;0x02:列车非阻塞;其他无效</td></tr><tr><td>列车激活端</td><td>1</td><td colspan="1">同《城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通接口规范第2部分:CBTC系统车地连续通信协议》中的定义</td></tr><tr><td>列车完整性</td><td>1</td><td colspan="1">0x01:完整;0x02:不完整;其他无效</td></tr><tr><td>列车紧急制动状态</td><td>1</td><td colspan="1">0x01:紧急制动;0x02:无紧急制动;其他无效</td></tr><tr><td>......</td><td></td><td></td><td colspan="1"></td></tr><tr><td>列车信息n</td><td></td><td></td><td colspan="1">n为“列车数量”字段取值</td></tr><tr><td>......</td><td></td><td></td><td></td><td></td></tr><tr><td>车站信息m</td><td></td><td></td><td></td><td>m为“车站信息个数”字段取值</td></tr><tr><td colspan="5">“列车阻塞”表示列车由于停车或低速行驶,处在某区间内时间是否超出设定时限(可设置)的状态信息。</td></tr></table>

# 5.2.3.3.5 列车运行调整信息包

对于跨线列车，线路ATS间应周期性互传各自线路内跨线运营分界处交出车站的计划运行图/时刻表、实迹运行图/时刻表和计划调整信息。互传信息内容见表6。

表 6 列车运行调整信息包  

<table><tr><td colspan="3">字 段</td><td>长度</td><td>说 明</td></tr><tr><td colspan="3">线路号</td><td>4</td><td>线路ID</td></tr><tr><td colspan="3">时间</td><td>9</td><td>本信息包产生时间。以数字表示年(2字节)、月、日、时、分、秒、毫秒(2字节)</td></tr><tr><td colspan="3">字 段</td><td>长度</td><td>说 明</td></tr><tr><td colspan="3">车站信息个数</td><td>1</td><td>信息包内车站个数</td></tr><tr><td rowspan="16">车站信息1</td><td colspan="2">站码</td><td>4</td><td>车站ID</td></tr><tr><td colspan="2">列车数量</td><td>2</td><td>本调度日内从该车站交出的列车数量</td></tr><tr><td rowspan="14">列车信息长度</td><td>列车信息长度</td><td>2</td><td>列车信息字节长度</td></tr><tr><td>源线路号</td><td>4</td><td>详见附录A.3</td></tr><tr><td>目的线路号</td><td>4</td><td>详见附录A.3</td></tr><tr><td>列车类型</td><td>1</td><td>1为计划车，2为头码车，3为人工车，其他无效</td></tr><tr><td>表号长度</td><td>1</td><td>数值</td></tr><tr><td>表号</td><td></td><td>字符，个数由表长度指定，详见附录A.3</td></tr><tr><td>车次号长度</td><td>1</td><td>数值</td></tr><tr><td>车次号</td><td></td><td>字符，个数由车次号长度指定，详见附录A.3</td></tr><tr><td>车组所属线路号</td><td>4</td><td>详见附录A.3</td></tr><tr><td>车组号长度</td><td>1</td><td>数值，详见附录A.3</td></tr><tr><td>车组号</td><td></td><td>字符，个数由车组号长度指定，详见附录A.3</td></tr><tr><td>目的地号长度</td><td>1</td><td>数值</td></tr><tr><td>目的地号</td><td></td><td>字符，个数由目的地号长度指定，详见附录A.3</td></tr><tr><td>运行方向</td><td>1</td><td>ATS系统内的列车运营方向0x01：下行；0x02：上行；0x00：未知；其他无效</td></tr><tr><td rowspan="7">车站信息1</td><td rowspan="5">列车信息1</td><td>预计交出时间</td><td>7</td><td>计划调整后的预计交出时间。以数字表示年(2字节)、月、日、时、分、秒,7个字节全为0表示列车已经实际交出。无计划信息时取值为0xFFFFEFXXXXXXXX</td></tr><tr><td>预计交出时刻的计划偏离时分</td><td>4</td><td colspan="1">表示计划在本线路调整完成后剩余的时间偏差值,也即需要下一线路ATS进行计划调整的时间偏差值,无计划信息列车按照准点处理。bit0~bit29为偏离时分数值,单位:s;bit30~bit31为早晚点标志,0为准点,1为早点,2为晚点</td></tr><tr><td>实际交出时间</td><td>7</td><td colspan="1">列车实际运行的交出时间。以数字表示年(2字节)、月、日、时、分、秒,7个字节全为0表示列车还未实际交出</td></tr><tr><td>实际交出时刻的计划偏离时分</td><td>4</td><td colspan="1">早晚点信息。无计划信息列车按照准点处理。bit0~bit29为偏离时分数值,单位:sbit30~bit31为早晚点标志,0为准点、1为早点、2为晚点</td></tr><tr><td>跨线区间的预计运行时间</td><td>2</td><td colspan="1">单位:s</td></tr><tr><td>......</td><td></td><td></td><td colspan="1"></td></tr><tr><td>列车信息n</td><td></td><td></td><td colspan="1">n为“列车数量”字段取值</td></tr><tr><td>......</td><td></td><td></td><td></td><td></td></tr><tr><td>车站信息m</td><td></td><td></td><td></td><td>m为“车站信息个数”字段取值</td></tr></table>

# 5.2.3.3.6 列车接入站跳停命令信息包

对跨线列车，当在接入线接入站（人工或自动）设置跳停时，应由接入线ATS发送站台跳停命令至至交出线ATS。当交出线ATS收到跳停命令后，应发送接收回执给接入站ATS，并应由交出站ATS负责管理接入站台的跳停命令和确定将命令发送至列车的时机，当回执超时且重发次数达到配置数量后应报警，并应停止发送。回执超时时间和重发次数均应可配置。跳停命令信息包见表7。

表 7 列车接入站跳停命令信息包  

<table><tr><td colspan="3">字 段</td><td>长度</td><td>说 明</td></tr><tr><td colspan="3">操作ID</td><td>16</td><td>UUID,命令唯一标识,每次人工/自动操作均有不同的ID</td></tr><tr><td colspan="3">接入站所在线路号</td><td>4</td><td>接入站所在线路ID</td></tr><tr><td colspan="3">接入站站码</td><td>4</td><td>接入站ID</td></tr><tr><td colspan="3">交出站所在线路号</td><td>4</td><td>交出站所在线路ID</td></tr><tr><td colspan="3">交出站站码</td><td>4</td><td>交出站ID</td></tr><tr><td colspan="3">时间</td><td>9</td><td>本信息包产生时间以数字表示年(2字节)、月、日、时、分、秒、毫秒(2字节)</td></tr><tr><td colspan="3">站台数量</td><td>2</td><td>数字</td></tr><tr><td rowspan="5">站台信息</td><td colspan="2">站台编号</td><td>2</td><td>数字,站台统一编号</td></tr><tr><td colspan="2">跳停类型</td><td>2</td><td>数字,1为无跳停,2为所有列车跳停,3为有指定列车跳停,0xFFFF为默认值,其他无效</td></tr><tr><td colspan="2">列车数量</td><td>2</td><td>数字,如跳停类型为1无跳停和2所有列车跳停,本字段应为0,跳停列车信息仅在跳停类型为指定列车跳停时有效</td></tr><tr><td rowspan="2">跳停列车信息1</td><td>源线路号</td><td>4</td><td>详见附录A.3</td></tr><tr><td>目的线路号</td><td>4</td><td>详见附录A.3</td></tr></table>

表 7 列车接入站跳停命令信息包 (表)  

<table><tr><td colspan="3">字 段</td><td>长度</td><td>说 明</td></tr><tr><td rowspan="10">站台信息</td><td rowspan="8">跳停列车信息1</td><td>表号长度</td><td>1</td><td>数值,表号长度和车次号长度为0时,表示指定车组跳停</td></tr><tr><td>表号</td><td></td><td>字符,个数由表长度指定,详见附录A.3</td></tr><tr><td>车次号长度</td><td>1</td><td>数值</td></tr><tr><td>车次号</td><td></td><td>字符,个数由车次号长度指定,详见附录A.3</td></tr><tr><td>车组所属线路号</td><td>4</td><td>详见附录A.3,车组号长度为0时无效</td></tr><tr><td>车组号长度</td><td>1</td><td>数字,车组号长度为0时,表示指定车次跳停,表号、车次号、车组号不能同时为空</td></tr><tr><td>车组号</td><td></td><td>字符,个数由车组号长度指定,详见附录A.3</td></tr><tr><td>下一停车站台编号</td><td></td><td>前方最近的停车站台编号,定义同站台编号,默认值为0xFFFF</td></tr><tr><td>......</td><td></td><td></td><td></td></tr><tr><td>跳停列车信息n</td><td></td><td></td><td>n为“列车数量”字段取值</td></tr><tr><td>......</td><td></td><td></td><td></td><td></td></tr><tr><td>下一站台信息</td><td></td><td></td><td></td><td></td></tr></table>

# 5.2.3.3.7 列车接入站跳停回执信息包

对跨线列车，当接入线接入站站台设置跳停时，交出线ATS在收到接入站发送的接入站站台跳停命令信息包后应回复接收回执。列车接入站跳停回执信息包见表8。

表 8 列车接入站跳停回执信息包  

<table><tr><td>字 段</td><td>长度</td><td>说 明</td></tr><tr><td>操作ID</td><td>16</td><td>UUID,命令唯一标识,与回复的命令ID相同</td></tr><tr><td>交出线路号</td><td>4</td><td>线路ID</td></tr><tr><td>交出线路名称长度</td><td>1</td><td>数值</td></tr><tr><td>交出线路名称</td><td></td><td>字符串</td></tr><tr><td>回执单位类型</td><td>1</td><td>01:车站02:中心其他无效</td></tr><tr><td>回执单位编码</td><td>2</td><td>单位类型为中心时,单位编码为调度台ID,服务器ID为0单位类型为车站时,单位编码为站码</td></tr><tr><td>回执单位名称长度</td><td>1</td><td>数值</td></tr><tr><td>回执单位名称</td><td></td><td>字符串</td></tr><tr><td>回执模块名称长度</td><td>1</td><td>数值</td></tr><tr><td>回执模块名称</td><td></td><td>字符串</td></tr><tr><td>回执发送时间</td><td>9</td><td>命令回执发送时的系统时间,以数字表示年、月、日、时、分、秒、毫秒(2字节)</td></tr><tr><td>接收结果状态</td><td>1</td><td>数值,0x01:接收成功,0x02:接收失败接收失败时,接收返回信息字段为失败原因,接收成功时,接收返回信息长度为0其他无效</td></tr><tr><td>接收返回信息长度</td><td>2</td><td>数值</td></tr><tr><td>接收返回信息</td><td></td><td>字符</td></tr><tr><td>预留信息长度</td><td>2</td><td>数值</td></tr><tr><td>预留信息</td><td></td><td>字节</td></tr></table>

# 5.2.3.3.8 ATS城市自定义信息包

自定义信息包用于实现各城市特有的互联互通相关功能。具体内容可在工程中根据实际需求约定。城市自定义信息包见表9。

表 9 ATS 城市自定义信息包  

<table><tr><td>字 段</td><td>长度</td><td>说 明</td></tr><tr><td>信息定义</td><td>N</td><td>具体内容在工程中约定</td></tr></table>

# 5.2.3.3.9 ATS厂商自定义信息包

自定义信息包用于实现各厂商特有功能，具体内容可由各厂商分别定制。发送方应判断当接收方与自身属于同一厂商时才可发送厂商自定义信息包。ATS收到非本厂商的厂商自定义信息包后，可不进行处理。厂商自定义信息包见表10。

表 10 ATS 厂商自定义信息包  

<table><tr><td>字 段</td><td>长度</td><td>说 明</td></tr><tr><td>信息定义</td><td>N</td><td>具体内容由各厂商分别定制</td></tr></table>

# 附录A

# （规范性附录）

# 设备类型定义、设备色码定义、列车信息识别号字段说明

# A.1 设备类型定义

表 A. 1 给出了设备类型定义。

表 A. 1 设备类型定义  

<table><tr><td>序号</td><td>设备类型</td><td>设备类型名称</td><td>备注</td></tr><tr><td>1</td><td>0x11</td><td>逻辑区段</td><td></td></tr><tr><td>2</td><td>0x16</td><td>物理区段</td><td></td></tr><tr><td>3</td><td>0x14</td><td>道岔</td><td></td></tr><tr><td>4</td><td>0x18</td><td>临时限速区段</td><td></td></tr><tr><td>5</td><td>0x21</td><td>信号机</td><td></td></tr><tr><td>6</td><td>0x31</td><td>按钮</td><td>例如,自动进路、自动触发等按钮</td></tr><tr><td>7</td><td>0x41</td><td>表示灯</td><td>例如,CI通道1、接口电源灯等表示灯,自动进路、自动触表示灯</td></tr><tr><td>8</td><td>0x42</td><td>联锁计数器</td><td>“联锁计数器”是指ATS界面上用于显示联锁倒计时(延时解锁等情况下)的设备</td></tr><tr><td>9</td><td>0x52</td><td>站台紧急关闭</td><td></td></tr><tr><td>10</td><td>0x54</td><td>安全门/屏蔽门</td><td></td></tr><tr><td>11</td><td>0x61</td><td>供电区段</td><td></td></tr></table>

# A.2 设备色码定义

# A.2.1 逻辑区段

表 A. 2 给出了逻辑区段定义。

表 A. 2 逻辑区段  

<table><tr><td>比特位</td><td>状态</td><td>值</td><td>说 明</td></tr><tr><td>0</td><td>通信故障状态</td><td>0:无故障1:有故障</td><td>ATS与联锁通信故障时的一种特殊状态表示</td></tr><tr><td>1</td><td>非通信列车占用状态</td><td>0:出清1:占用</td><td></td></tr><tr><td>2</td><td>锁闭状态</td><td>0:非锁闭1:锁闭</td><td></td></tr><tr><td>3</td><td>故障锁闭</td><td>0:非故障锁闭1:故障锁闭</td><td></td></tr><tr><td>4</td><td>封锁状态</td><td>0:非封锁1:封锁</td><td></td></tr><tr><td>5</td><td>CBTC通信列车占用状态</td><td>0:出清1:占用</td><td></td></tr><tr><td>6</td><td>保护区段锁闭</td><td>0:非锁闭1:锁闭</td><td></td></tr><tr><td>7</td><td>区段切除</td><td>0:非切除1:切除</td><td></td></tr><tr><td>8,9</td><td>预留</td><td></td><td></td></tr><tr><td>10</td><td>计轴复位</td><td>0:无计轴复位(或默认值)1:有计轴复位</td><td>若ATS没有此信息,应发送默认值,作为信息接收方时可不处理本字段</td></tr><tr><td>11</td><td>预留</td><td></td><td></td></tr><tr><td>12,13</td><td>预留</td><td></td><td></td></tr><tr><td>14,15</td><td>预留</td><td></td><td></td></tr><tr><td>16~22</td><td>预留</td><td></td><td></td></tr><tr><td>23</td><td>ARB故障</td><td>0:无故障1:有故障</td><td></td></tr><tr><td>24,25</td><td>OD占用</td><td>00:默认01:非法10:出清11:占用</td><td>若ATS没有此信息,应发送默认值,作为信息接收方时可不处理本字段</td></tr><tr><td>26~31</td><td>预留</td><td></td><td></td></tr></table>

# A.2.2 物理区段

如没有该信息，可不用发送此类设备信息。表A.3给出了物理区段定义。

表 A. 3 物理区段  

<table><tr><td>比特位</td><td>状态</td><td>值</td><td>说 明</td></tr><tr><td>0</td><td>通信故障状态</td><td>0:无故障1:有故障</td><td>ATS与联锁通信故障时的一种特殊状态表示</td></tr><tr><td>1</td><td>故障锁闭</td><td>0:非故障锁闭1:故障锁闭</td><td></td></tr><tr><td>2</td><td>区段切除</td><td>0:非切除1:切除</td><td></td></tr><tr><td>3</td><td>计轴复位</td><td>0:计轴复位1:计轴未复位</td><td></td></tr><tr><td>4~7</td><td>预留</td><td></td><td></td></tr></table>

# A.2.3 道岔

表 A. 4 给出了道岔定义。

表 A. 4 道岔  

<table><tr><td>比特位</td><td>状态</td><td>值</td><td>说明</td></tr><tr><td>0</td><td>通信故障状态</td><td>0:无故障1:有故障</td><td>ATS与联锁通信故障时的一种特殊状态表示</td></tr><tr><td>1</td><td>非通信列车占用状态</td><td>0:出清1:占用</td><td></td></tr><tr><td>2</td><td>锁闭状态</td><td>0:非锁闭1:锁闭</td><td></td></tr><tr><td>3</td><td>故障锁闭</td><td>0:非故障锁闭1:故障锁闭</td><td></td></tr><tr><td>4,5</td><td>道岔位置</td><td>00:四开(无表示)01:定位10:反位11:挤岔</td><td></td></tr><tr><td>6</td><td>单锁状态</td><td>0:非单锁1:单锁</td><td></td></tr><tr><td>7</td><td>单封状态</td><td>0:非单封1:单封</td><td></td></tr><tr><td>8</td><td>CBTC通信列车占用状态</td><td>0:出清1:占用</td><td></td></tr><tr><td>9</td><td>保护区段锁闭</td><td>0:非锁闭1:锁闭</td><td></td></tr><tr><td>10</td><td>轨道区段切除</td><td>0:非切除1:切除</td><td></td></tr><tr><td>11</td><td>区段封锁状态</td><td>0:非封锁1:封锁</td><td></td></tr><tr><td>12~18</td><td>预留</td><td></td><td></td></tr><tr><td>19,20</td><td>预留</td><td></td><td></td></tr><tr><td>21,22</td><td>预留</td><td></td><td></td></tr><tr><td>23~29</td><td>预留</td><td></td><td></td></tr><tr><td>30</td><td>ARB故障</td><td>0:无故障1:有故障</td><td></td></tr><tr><td>31,32</td><td>OD占用</td><td>00:默认01:非法10:出清11:占用</td><td>若ATS没有此信息,应发送默认值,作为信息接收方时可不处理本字段</td></tr><tr><td>33~39</td><td>预留</td><td></td><td></td></tr></table>

# A.2.4 临时限速区段

表A.5给出了临时限速区段定义。

表 A. 5 临时限速区段  

<table><tr><td>比特位</td><td>状态</td><td>值</td><td>说 明</td></tr><tr><td>0</td><td>信息标志位</td><td>0:状态信息无效,临时限速状态为未知1:状态信息有效</td><td>表示ATS间此临时限速区段信息是否有效</td></tr><tr><td>1,2</td><td>CI限速状态</td><td>00:无限速01:限速验证通过10:限速执行成功11:取消验证通过</td><td>若ATS没有限速验证通过、取消验证通过状态,作为信息接收方时可不处理本字段的上述状态</td></tr><tr><td>3,4</td><td>ATP限速状态</td><td>00:无限速01:限速验证通过10:限速执行成功11:取消验证通过</td><td>若ATS没有限速验证通过、取消验证通过状态,作为信息接收方时可不处理本字段的上述状态</td></tr><tr><td>5~11</td><td>ATP限速等级</td><td>数值,限速值(0~128km/h),0为无效值</td><td></td></tr><tr><td>12~15</td><td>预留</td><td></td><td></td></tr></table>

# A.2.5 信号机

信号机的颜色可用两位（高位、低位，低位为靠近灯柱位置，高位为远离灯柱的位置）的颜色组合来表示，表示方法如下：

a）室外信号机关闭：高位、低位均为无色；  
b）一个颜色：比如绿——高位无色、低位为绿；  
c）两个颜色：比如红白——高位为红、低位为白。

表A.6给出了信号机定义。  
表 A. 6 信号机  

<table><tr><td>比特位</td><td>状态</td><td>值</td><td>说 明</td></tr><tr><td>0</td><td>通信故障状态</td><td>0:无故障1:有故障</td><td>ATS与联锁通信故障时的一种特殊状态表示</td></tr><tr><td>1~4</td><td>低位颜色</td><td>0x00:无色0x01:绿0x02:黄0x03:红0x04:白0x05:蓝0x06:灰0x07:紫0x08:黑0x09:橙0x0a:青0x0b~0x0f:预留</td><td></td></tr><tr><td>5</td><td>低位闪烁</td><td>0:无闪烁1:闪烁</td><td></td></tr><tr><td>6~9</td><td>高位颜色</td><td>取值同“低位颜色”</td><td></td></tr><tr><td>10</td><td>高位闪烁</td><td>0:无闪烁1:闪烁</td><td></td></tr><tr><td>12</td><td>室外信号机关闭</td><td>0:非关闭1:关闭</td><td></td></tr><tr><td>14</td><td>屏蔽一次临时限速</td><td>0:无屏蔽一次临时限速1:屏蔽一次临时限速</td><td>点式、联锁等级下进路内存在有临时限速的区段时,进路始端信号机不开放,屏蔽一次临时限速命令可开放始端信号机。一次有效。本项表示信号机有或无屏蔽一次临时限速的状态,默认值为0</td></tr><tr><td>15</td><td>预留</td><td></td><td></td></tr><tr><td>20~23</td><td>预留</td><td>预留</td><td></td></tr></table>

# A.2.6 按钮

表 A. 7 给出了按钮定义。

表 A. 7 按钮  

<table><tr><td>比特位</td><td>状态</td><td>值</td><td>说 明</td></tr><tr><td>0</td><td>通信故障状态</td><td>0:无故障1:有故障</td><td>ATS与联锁通信故障时的一种特殊状态表示</td></tr><tr><td>1</td><td>按下状态</td><td>0:弹起1:按下</td><td></td></tr><tr><td>2</td><td>闪烁</td><td>预留</td><td></td></tr><tr><td>3</td><td>封锁状态</td><td>预留</td><td></td></tr><tr><td>4~7</td><td>预留</td><td>预留</td><td></td></tr></table>

# A.2.7 联锁计数器

表 A. 8 给出了联锁计数器定义。

表 A. 8 联锁计数器  

<table><tr><td>比特位</td><td>状态</td><td>值</td><td>说 明</td></tr><tr><td>0</td><td>通信故障状态</td><td>0:无故障1:有故障</td><td>表示 ATS 与联锁通信故障时的一种特殊状态表示</td></tr><tr><td>1~8</td><td>计时值</td><td>0~255</td><td>计时单位:s</td></tr><tr><td>9~15</td><td>预留</td><td>预留</td><td></td></tr></table>

# A.2.8 表示灯

表 A. 9 给出了表示灯定义。

表 A. 9 表示灯  

<table><tr><td>比特位</td><td>状态</td><td>值</td><td>说 明</td></tr><tr><td>0</td><td>通信故障状态</td><td>0:无故障1:有故障</td><td>ATS与联锁通信故障时的一种特殊状态表示</td></tr><tr><td>1~4</td><td>颜色</td><td>0x00:无色0x01:绿0x02:黄0x03:红0x04:白0x05:蓝0x06:灰0x07:紫0x08:黑0x09:橙0x0a:青0x0b~0x0f:预留</td><td></td></tr><tr><td>5</td><td>闪烁</td><td>0:无闪烁1:闪烁</td><td></td></tr><tr><td>6,7</td><td>预留</td><td>预留</td><td></td></tr></table>

# A.2.9 站台紧急关闭

表 A. 10 给出了站台紧急关闭定义。

表 A. 10 站台紧急关闭  

<table><tr><td>比特位</td><td>状态</td><td>值</td><td>说 明</td></tr><tr><td>0</td><td>通信故障状态</td><td>0:无故障1:有故障</td><td>ATS与联锁通信故障时的一种特殊状态表示</td></tr><tr><td>1</td><td>站台紧急关闭</td><td>0:无1:有</td><td></td></tr><tr><td>2~7</td><td>预留</td><td>预留</td><td></td></tr></table>

# A.2.10 安全门/屏蔽门

表 A. 11 给出了安全门/屏蔽门定义。

表 A. 11 安全门/屏蔽门  

<table><tr><td>比特位</td><td>状态</td><td>值</td><td>说 明</td></tr><tr><td>0</td><td>通信故障状态</td><td>0:无故障1:有故障</td><td>ATS与联锁通信故障时的一种特殊状态表示</td></tr><tr><td>1,2</td><td>门状态</td><td>00:正常关门01:正常开门10:旁路关门11:旁路开门</td><td>若ATS没有旁路关门和旁路开门状态,作为信息接收方时以上两种状态宜按照正常关门处理</td></tr><tr><td>3~7</td><td>预留</td><td>预留</td><td></td></tr></table>

# A.2.11 供电区段

表A.12给出了供电区段定义。

表 A. 12 供电区段  

<table><tr><td>比特位</td><td>状态</td><td>值</td><td>说 明</td></tr><tr><td>0</td><td>通信故障状态</td><td>0:无故障1:有故障</td><td>ATS与联锁通信故障时的一种特殊状态表示</td></tr><tr><td>1,2</td><td>供电状态</td><td>00:未知01:通电10:断电</td><td></td></tr><tr><td>3~7</td><td>预留</td><td>预留</td><td></td></tr></table>

# A.3 列车信息识别号字段说明

表A.13给出了列车信息识别号字段说明定义。

表 A. 13 列车信息识别号字段说明  

<table><tr><td>内容</td><td>说 明</td></tr><tr><td>源线路号</td><td>列车始发所在线路号,可由字母或数字组成,非跨线列车源线路号与日的线路号相同</td></tr><tr><td>日的线路号</td><td>列车终到所在线路号,可由字母或数字组成,非跨线列车日的线路号与源线路号相同</td></tr><tr><td>列车类型</td><td>1为计划车;2为头码车;3为人工车;其他无效</td></tr><tr><td>表号</td><td>由两位数字或三位数字组成,默认值为“00”或“000”</td></tr><tr><td>车次号</td><td>由四位数字组成,默认值为“0000”,有效范围 0001 ~9999。9000~9999作为预留车次范围(车次号范围定义可按照业主需求进行配置)</td></tr><tr><td>车组所属线路号</td><td>车组所属线路号,可由字母或数字组成</td></tr><tr><td>车组号</td><td>由三位数字组成,有效范围 001~999,车组所属线路号+车组号应在互联互通线路内唯一</td></tr><tr><td>目的地号</td><td>可由字母或数字组成,目的线路号+目的地号在互联互通线路内应统一定义</td></tr><tr><td>运行方向</td><td>ATS系统内的列车运营方向0x01:下行;0x02:上行;0x00:未知;其他无效</td></tr></table>

中国城市轨道交通协会团体标准

城市轨道交通 基于通信的列车运行

控制系统（CBTC）互联互通接口规范

第6部分：列车自动监控系统（ATS）间接口

T/CAMET 04011.6—2018

\*

中国铁道出版社有限公司出版发行

（100054，北京市西城区右安门西街8号）

公司网址：http://www.tdpress.com

北京铭成印刷有限公司印刷

开本：  $880~\mathrm{mm}\times 1230~\mathrm{mm}$  1/32印张：t.375字数：36千

2019年5月第1版 2019年5月第1次印刷

书号：15113·5732 定价：15.00元

版权所有 侵权必究

凡购买铁道版图书，如有印制质量问题，请与本公司发行部联系调换。

发行部电话：路（021）73174，市（010）51873174