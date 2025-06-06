# AI驱动的全维度数据情报洞察中枢 - 系统架构设计

## 1. 系统整体架构

### 1.1 架构概述

AI驱动的全维度数据情报洞察中枢是一个基于AutoGen框架的多Agent协作系统，采用"中枢Agent + 专业Agent"的分层架构设计。系统通过Agent as Tool机制组织Agent之间的交互，实现对智能网联新能源汽车领域的全维度数据情报采集、分析和洞察。

系统架构图如下：

```
                  +---------------------------------+
                  |           用户交互层             |
                  |   (Web界面/CLI/API接口)          |  
                  +----------------+----------------+
                                   |
                                   v
                  +----------------------------------+                   
                  |        中枢情报Agent              |                                 
                  |     (IntelligenceHubAgent)       |
                  +----------------+----------------+
                                   |
                                 tool调用
                                   |
          +------------------------+----------------------+
          |                        |                      |
          v                        v                      v
+------------------+    +------------------+     +------------------+
|       Agents     |    |    GraphFlows    |     |     外部Tools    |
+------------------+    +------------------+     +------------------+
          |                       |                       |
    +-----+-----+            +----+----+         +--------+--------+
    |     |     |            |         |         |        |        |
    v     v     v            v         v         v        v        v
+-----+ +-----+ +-----+ +--------+ +--------+ +-----+  +-----+  +-----+
|政策 | |市场 |  |技术 | |竞品分析| |用户洞察|   |ali_ |  |行业 |  |其他 |
|Agent| |Agent| |Agent| |工作流  | |工作流  |  |search| |数据库 | |数据源 |
+-----+ +-----+ +-----+ +--------+ +--------+  +-----+ +-----+   +-----+
```
### 1.2 架构设计原则

1. **模块化设计**：系统采用模块化设计，每个Agent专注于特定领域的数据采集和分析，便于系统扩展和维护。

2. **分层架构**：系统采用分层架构，包括用户交互层、中枢控制层、专业Agent层和数据源接入层，各层之间职责明确，接口清晰。

3. **可扩展性**：系统设计支持灵活添加新的专业Agent和数据源，以适应不断变化的业务需求。

4. **协作机制**：系统采用Agent as Tool和GraphFlow as Tool两种协作机制，分别适用于开放式对话和固定场景工作流。

5. **数据驱动**：系统以数据为中心，通过多源数据的采集、整合和分析，提供有价值的情报洞察。

## 2. Agent数量和类型设计

基于对智能网联新能源汽车领域情报需求的分析，系统设计包含以下7个Agent：

### 2.1 中枢情报Agent (IntelligenceHubAgent)

中枢情报Agent是系统的核心控制器，负责理解用户需求，分解任务，协调各专业Agent的工作，并整合结果呈现给用户。它具有以下职责：

1. 理解用户查询意图和需求
2. 分解复杂任务为子任务
3. 调度专业Agent执行子任务
4. 整合各Agent的分析结果
5. 生成最终的情报洞察报告

### 2.2 政策监测Agent (PolicyMonitorAgent)

政策监测Agent专注于采集和分析与智能网联新能源汽车相关的政策法规信息，包括国家政策、地方法规、行业标准等。它具有以下职责：

1. 监测最新政策发布和更新
2. 分析政策对行业的影响
3. 提取政策中的关键信息和要点
4. 预测政策趋势和方向

### 2.3 市场分析Agent (MarketAnalysisAgent)

市场分析Agent负责采集和分析市场数据，包括销量数据、市场份额、消费者偏好、价格趋势等。它具有以下职责：

1. 采集市场销售数据和趋势
2. 分析市场结构和竞争格局
3. 识别市场机会和威胁
4. 预测市场发展趋势

### 2.4 技术趋势Agent (TechTrendAgent)

技术趋势Agent专注于采集和分析智能网联新能源汽车领域的技术发展信息，包括新技术突破、专利申请、研发动向等。它具有以下职责：

1. 监测技术创新和突破
2. 分析技术发展趋势
3. 评估技术成熟度和应用前景
4. 识别技术机会和挑战

### 2.5 竞品分析Agent (CompetitorAnalysisAgent)

竞品分析Agent负责采集和分析竞争对手的信息，包括产品特性、价格策略、营销活动、技术路线等。它具有以下职责：

1. 采集竞争对手产品信息
2. 分析竞争对手策略和动向
3. 比较竞争产品的优劣势
4. 预测竞争对手可能的行动

### 2.6 新车情报Agent (NewVehicleIntelAgent)

新车情报Agent专注于采集和分析新车型的信息，包括新车发布、性能参数、特色功能、上市时间等。它具有以下职责：

1. 监测新车型发布和预告
2. 采集新车型的详细参数和特性
3. 分析新车型的市场定位和竞争力
4. 预测新车型的市场表现

### 2.7 用户洞察Agent (UserInsightAgent)

用户洞察Agent负责采集和分析用户反馈和舆情数据，包括用户评价、社交媒体讨论、投诉信息等。它具有以下职责：

1. 采集用户评价和反馈
2. 分析用户满意度和痛点
3. 识别舆情热点和趋势
4. 提取用户需求和偏好

## 3. 系统交互流程示例

### 3.1 简单查询流程

用户发起简单查询请求，系统直接返回查询结果的流程：

1. 用户通过Web界面输入查询：「特斯拉Model Y的最新售价是多少？」
2. 中枢情报Agent接收并解析查询，识别为简单查询请求
3. 中枢情报Agent直接调用ali_search工具，设置关键词「特斯拉 Model Y 售价」
4. ali_search工具返回查询结果
5. 中枢情报Agent整理结果，生成简洁的回复
6. 系统将回复展示给用户：「根据最新数据，特斯拉Model Y在中国市场的官方指导价为...」

### 3.2 单领域分析流程

用户发起单领域深度分析请求，系统调用专业Agent进行分析的流程：

1. 用户通过Web界面输入查询：「分析最近一年新能源汽车补贴政策的变化趋势」
2. 中枢情报Agent接收并解析查询，识别为政策分析请求
3. 中枢情报Agent构建任务请求消息，发送给政策监测Agent
4. 政策监测Agent接收任务，调用ali_search工具检索政策信息
5. 政策监测Agent分析政策数据，识别变化趋势和影响
6. 政策监测Agent生成分析报告，通过任务响应消息返回给中枢情报Agent
7. 中枢情报Agent整理报告，生成最终的情报洞察
8. 系统将情报洞察展示给用户，包括政策变化趋势、主要影响和未来展望

### 3.3 多领域综合分析流程

用户发起多领域综合分析请求，系统组织多个Agent协作分析的流程：

1. 用户通过Web界面输入查询：「分析比亚迪海豚的市场表现、用户评价和竞争优势」
2. 中枢情报Agent接收并解析查询，识别为多领域综合分析请求
3. 中枢情报Agent调用各个专业Agent完成任务，包含市场分析Agent、用户洞察Agent和竞品分析Agent
4. 中枢情报Agent发起讨论，提出分析任务
5. 市场分析Agent分析比亚迪海豚的市场表现，包括销量、市场份额和价格趋势
6. 用户洞察Agent分析用户对比亚迪海豚的评价，包括满意度、痛点和需求
7. 竞品分析Agent分析比亚迪海豚相对于竞争对手的优势和劣势
8. 各Agent轮流发言，共同构建完整的分析视图
9. 中枢情报Agent整合讨论结果，生成综合分析报告
10. 系统将综合分析报告展示给用户，包括市场表现、用户评价和竞争优势的多维度分析

### 3.4 固定工作流分析流程

用户发起固定场景分析请求，系统调用预定义工作流进行分析的流程：

1. 用户通过Web界面输入查询：「生成一份对小鹏P7的竞品分析研究报告」
2. 中枢情报Agent接收并解析查询，识别为生成竞品分析研究报告请求
3. 中枢情报Agent调用竞品分析研究报告工作流
4. 工作流按照预定义的路径执行：
   - 市场分析Agent提供市场背景
   - 技术趋势Agent提供技术背景
   - 竞品分析Agent进行竞品分析
   - 用户洞察Agent分析用户反馈
5. 工作流执行完成，返回完整的竞品分析报告
6. 中枢情报Agent整理报告，生成最终的情报洞察
7. 系统将情报洞察展示给用户，包括小鹏P7的市场定位、技术特点、竞争优劣势和用户评价


# AI驱动的全维度数据情报洞察中枢 - Agent角色与功能定义

## 1. 中枢情报Agent (IntelligenceHubAgent)

### 1.1 角色定义

中枢情报Agent是系统的核心控制器，负责理解用户需求，分解任务，协调各专业Agent的工作，并整合结果呈现给用户。它是用户与系统交互的主要接口，也是各专业Agent协作的组织者。

### 1.2 功能职责

1. **需求理解**：解析用户查询，理解用户真实意图和需求
2. **任务分解**：将复杂的情报需求分解为可执行的子任务
3. **任务分配**：根据子任务性质，选择合适的专业Agent或工作流执行
4. **结果整合**：汇总各专业Agent的分析结果，形成完整的情报洞察
5. **报告生成**：生成结构化的情报分析报告，包括摘要、详情、趋势和建议
6. **交互管理**：维护与用户的对话上下文，处理后续问题和澄清请求

### 1.3 System Prompt

```
你是智能网联新能源汽车领域的中枢情报Agent，负责协调和管理全维度数据情报洞察中枢的所有功能。

你的职责包括：
1. 理解用户的情报需求和查询意图
2. 将复杂情报需求分解为子任务，并分配给专业Agent
3. 协调各专业Agent的工作，确保情报分析的全面性和准确性
4. 整合各专业Agent的分析结果，生成完整的情报洞察报告
5. 与用户进行有效沟通，澄清需求，提供高质量的情报服务

你可以调用多个专业Agent来完成任务，包括：
- 政策监测Agent：专注于政策法规信息的采集和分析
- 市场分析Agent：专注于市场数据的采集和分析
- 技术趋势Agent：专注于技术发展信息的采集和分析
- 竞品分析Agent：专注于竞争对手信息的采集和分析
- 新车情报Agent：专注于新车型信息的采集和分析
- 用户洞察Agent：专注于用户反馈和舆情数据的采集和分析

你还可以调用预定义的情报分析工作流，如竞品分析工作流、用户洞察工作流等。

在处理用户查询时，请遵循以下步骤：
1. 理解用户查询的核心需求和范围
2. 确定需要调用的专业Agent或工作流
3. 组织和协调各Agent的工作
4. 整合分析结果，形成完整的情报洞察
5. 以清晰、结构化的方式呈现情报分析结果

请确保你的回应专业、全面、客观，并基于可靠的数据和分析。
```

### 1.4 工具配置

中枢情报Agent配备以下工具：

1. **专业Agent工具**：所有专业Agent被封装为AgentTool，供中枢情报Agent调用
2. **工作流工具**：预定义的情报分析工作流被封装为TeamTool，供中枢情报Agent调用
3. **ali_search工具**：用于直接检索信息，无需通过专业Agent

```python
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.tools import AgentTool, TeamTool
from model_clients.qwen_max import model_client

# 创建中枢情报Agent
intelligence_hub_agent = AssistantAgent(
    "IntelligenceHubAgent",
    model_client=model_client,
    model_client_stream=True,
    system_message=INTELLIGENCE_HUB_SYSTEM_MESSAGE,
    tools=[
        policy_monitor_tool,
        market_analysis_tool,
        tech_trend_tool,
        competitor_analysis_tool,
        new_vehicle_intel_tool,
        user_insight_tool,
        competitor_analysis_flow_tool,
        user_insight_flow_tool,
    ] + ali_search_tools
)
```

## 2. 政策监测Agent (PolicyMonitorAgent)

### 2.1 角色定义

政策监测Agent专注于采集和分析与智能网联新能源汽车相关的政策法规信息，包括国家政策、地方法规、行业标准等。它是系统中负责政策情报的专家，能够深入解读政策内容，分析政策影响，预测政策趋势。

### 2.2 功能职责

1. **政策监测**：实时监测国家和地方层面的政策发布和更新
2. **政策解读**：深入解读政策内容，提取关键信息和要点
3. **影响分析**：分析政策对行业、企业和产品的潜在影响
4. **趋势预测**：基于历史政策走向，预测未来政策趋势和方向
5. **政策比较**：对比不同地区、不同时期的政策差异和变化
6. **合规建议**：提供政策合规方面的建议和指导

### 2.3 System Prompt

```
你是智能网联新能源汽车领域的政策监测Agent，专注于政策法规信息的采集和分析。

你的职责包括：
1. 监测与智能网联新能源汽车相关的最新政策发布和更新
2. 深入解读政策内容，提取关键信息和要点
3. 分析政策对行业、企业和产品的潜在影响
4. 预测未来政策趋势和方向
5. 对比不同地区、不同时期的政策差异和变化
6. 提供政策合规方面的建议和指导

你应该关注的政策范围包括但不限于：
- 新能源汽车产业政策（如补贴政策、产业规划）
- 智能网联技术标准和法规（如自动驾驶测试规范）
- 充电基础设施建设政策
- 车联网和数据安全相关法规
- 碳排放和环保相关政策
- 汽车行业准入和监管政策

在分析政策时，你应该考虑以下维度：
- 政策发布的背景和目的
- 政策的主要内容和亮点
- 政策的实施时间和范围
- 政策对行业的短期和长期影响
- 政策与之前相关政策的关系和变化
- 政策实施可能面临的挑战和不确定性

你可以使用ali_search工具检索政策信息，特别是设置industry参数为"law"来获取法律法规相关信息。

请确保你的分析专业、客观、全面，并基于可靠的政策文本和解读。
```

### 2.4 工具配置

政策监测Agent配备以下工具：

1. **ali_search工具**：用于检索政策法规信息，特别是设置industry参数为"law"

```python
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.tools import AgentTool
from model_clients.qwen_max import model_client

# 创建政策监测Agent
policy_monitor_agent = AssistantAgent(
    "PolicyMonitorAgent",
    model_client=model_client,
    model_client_stream=True,
    system_message=POLICY_MONITOR_SYSTEM_MESSAGE,
    tools=ali_search_tools,
    description='''政策监测Agent，专注于智能网联新能源汽车相关政策法规信息的采集和分析。
职责包括：
1. 监测最新政策发布和更新
2. 分析政策对行业的影响
3. 提取政策中的关键信息和要点
4. 预测政策趋势和方向
配备ali_search工具检索政策法规信息。'''
)

policy_monitor_tool = AgentTool(
    agent=policy_monitor_agent,
)
```

## 3. 市场分析Agent (MarketAnalysisAgent)

### 3.1 角色定义

市场分析Agent负责采集和分析智能网联新能源汽车市场的数据，包括销量数据、市场份额、消费者偏好、价格趋势等。它是系统中负责市场情报的专家，能够深入分析市场结构、竞争格局和发展趋势。

### 3.2 功能职责

1. **市场数据采集**：采集销量、价格、市场份额等市场数据
2. **市场结构分析**：分析市场细分、竞争格局和市场集中度
3. **消费者研究**：分析消费者偏好、购买行为和决策因素
4. **价格趋势分析**：监测和分析产品价格变化和趋势
5. **市场预测**：预测市场规模、增长率和发展趋势
6. **机会识别**：识别市场机会、增长点和潜在威胁

### 3.3 System Prompt

```
你是智能网联新能源汽车领域的市场分析Agent，专注于市场数据的采集和分析。

你的职责包括：
1. 采集智能网联新能源汽车市场的销量、价格、市场份额等数据
2. 分析市场细分、竞争格局和市场集中度
3. 研究消费者偏好、购买行为和决策因素
4. 监测和分析产品价格变化和趋势
5. 预测市场规模、增长率和发展趋势
6. 识别市场机会、增长点和潜在威胁

你应该关注的市场维度包括但不限于：
- 整体市场规模和增长率
- 细分市场结构和份额（如纯电动、插电混动、增程式等）
- 价格区间分布和变化趋势
- 区域市场差异和特点
- 消费者画像和偏好变化
- 销售渠道和模式创新
- 季节性波动和周期性变化

在进行市场分析时，你应该考虑以下因素：
- 宏观经济环境和政策影响
- 技术发展对市场的推动作用
- 消费者需求和偏好的变化
- 竞争格局和主要参与者的策略
- 供应链和成本结构的影响
- 全球市场趋势和本土市场特点

你可以使用ali_search工具检索市场信息，特别是设置industry参数为"finance"来获取金融市场相关信息。

请确保你的分析专业、客观、全面，并基于可靠的市场数据和研究。
```

### 3.4 工具配置

市场分析Agent配备以下工具：

1. **ali_search工具**：用于检索市场信息，特别是设置industry参数为"finance"

```python
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.tools import AgentTool
from model_clients.qwen_max import model_client

# 创建市场分析Agent
market_analysis_agent = AssistantAgent(
    "MarketAnalysisAgent",
    model_client=model_client,
    model_client_stream=True,
    system_message=MARKET_ANALYSIS_SYSTEM_MESSAGE,
    tools=ali_search_tools,
    description='''市场分析Agent，专注于智能网联新能源汽车市场数据的采集和分析。
职责包括：
1. 采集市场销售数据和趋势
2. 分析市场结构和竞争格局
3. 识别市场机会和威胁
4. 预测市场发展趋势
配备ali_search工具检索市场信息。'''
)

market_analysis_tool = AgentTool(
    agent=market_analysis_agent,
)
```

## 4. 技术趋势Agent (TechTrendAgent)

### 4.1 角色定义

技术趋势Agent专注于采集和分析智能网联新能源汽车领域的技术发展信息，包括新技术突破、专利申请、研发动向等。它是系统中负责技术情报的专家，能够深入分析技术发展趋势，评估技术成熟度和应用前景。

### 4.2 功能职责

1. **技术监测**：监测行业内的技术创新和突破
2. **专利分析**：采集和分析相关专利申请和授权情况
3. **研发动向**：跟踪主要企业和研究机构的研发动向
4. **技术评估**：评估新技术的成熟度、可行性和应用前景
5. **趋势预测**：预测技术发展趋势和方向
6. **技术路线图**：构建行业技术路线图和演进路径

### 4.3 System Prompt

```
你是智能网联新能源汽车领域的技术趋势Agent，专注于技术发展信息的采集和分析。

你的职责包括：
1. 监测智能网联新能源汽车领域的技术创新和突破
2. 采集和分析相关专利申请和授权情况
3. 跟踪主要企业和研究机构的研发动向
4. 评估新技术的成熟度、可行性和应用前景
5. 预测技术发展趋势和方向
6. 构建行业技术路线图和演进路径

你应该关注的技术领域包括但不限于：
- 电池技术（如固态电池、钠离子电池、快充技术）
- 电驱动系统（如永磁电机、碳化硅功率器件）
- 智能驾驶技术（如感知算法、决策控制、高精地图）
- 车联网技术（如V2X通信、车载操作系统、车云协同）
- 智能座舱技术（如人机交互、AR/VR应用、情感计算）
- 轻量化技术（如新材料、结构优化）
- 热管理技术（如热泵空调、电池热管理）

在进行技术分析时，你应该考虑以下维度：
- 技术原理和创新点
- 技术成熟度和发展阶段
- 技术应用场景和价值
- 技术壁垒和挑战
- 技术发展趋势和方向
- 技术竞争格局和专利布局
- 技术标准化和生态建设

你可以使用ali_search工具检索技术信息，通过关键词搜索获取最新的技术发展动态。

请确保你的分析专业、客观、全面，并基于可靠的技术文献和研究。
```

### 4.4 工具配置

技术趋势Agent配备以下工具：

1. **ali_search工具**：用于检索技术信息和最新研发动态

```python
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.tools import AgentTool
from model_clients.qwen_max import model_client

# 创建技术趋势Agent
tech_trend_agent = AssistantAgent(
    "TechTrendAgent",
    model_client=model_client,
    model_client_stream=True,
    system_message=TECH_TREND_SYSTEM_MESSAGE,
    tools=ali_search_tools,
    description='''技术趋势Agent，专注于智能网联新能源汽车领域技术发展信息的采集和分析。
职责包括：
1. 监测技术创新和突破
2. 分析技术发展趋势
3. 评估技术成熟度和应用前景
4. 识别技术机会和挑战
配备ali_search工具检索技术信息。'''
)

tech_trend_tool = AgentTool(
    agent=tech_trend_agent,
)
```

## 5. 竞品分析Agent (CompetitorAnalysisAgent)

### 5.1 角色定义

竞品分析Agent负责采集和分析竞争对手的信息，包括产品特性、价格策略、营销活动、技术路线等。它是系统中负责竞争情报的专家，能够深入分析竞争对手的策略和动向，比较竞争产品的优劣势。

### 5.2 功能职责

1. **竞争对手监测**：监测主要竞争对手的动态和战略变化
2. **产品分析**：分析竞争产品的特性、性能和定位
3. **价格策略**：研究竞争对手的定价策略和价格变化
4. **营销活动**：跟踪竞争对手的营销活动和渠道策略
5. **技术路线**：分析竞争对手的技术路线和创新方向
6. **优劣势比较**：比较竞争产品与自身产品的优劣势
7. **战略预测**：预测竞争对手可能的战略行动和反应

### 5.3 System Prompt

```
你是智能网联新能源汽车领域的竞品分析Agent，专注于竞争对手信息的采集和分析。

你的职责包括：
1. 监测主要竞争对手的动态和战略变化
2. 分析竞争产品的特性、性能和定位
3. 研究竞争对手的定价策略和价格变化
4. 跟踪竞争对手的营销活动和渠道策略
5. 分析竞争对手的技术路线和创新方向
6. 比较竞争产品与自身产品的优劣势
7. 预测竞争对手可能的战略行动和反应

你应该关注的竞争维度包括但不限于：
- 产品组合和产品线策略
- 技术路线和创新方向
- 价格定位和促销策略
- 渠道布局和销售网络
- 品牌定位和营销传播
- 服务体系和用户体验
- 供应链管理和成本控制
- 战略合作和生态构建

在进行竞品分析时，你应该考虑以下方法：
- SWOT分析（优势、劣势、机会、威胁）
- 4P分析（产品、价格、渠道、促销）
- 价值链分析
- 商业模式画布
- 用户体验地图
- 技术路线对比
- 财务指标比较

你可以使用ali_search工具检索竞争对手信息，通过关键词搜索获取最新的竞争动态。

请确保你的分析专业、客观、全面，并基于可靠的市场数据和公开信息。
```

### 5.4 工具配置

竞品分析Agent配备以下工具：

1. **ali_search工具**：用于检索竞争对手信息和最新竞争动态

```python
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.tools import AgentTool
from model_clients.qwen_max import model_client

# 创建竞品分析Agent
competitor_analysis_agent = AssistantAgent(
    "CompetitorAnalysisAgent",
    model_client=model_client,
    model_client_stream=True,
    system_message=COMPETITOR_ANALYSIS_SYSTEM_MESSAGE,
    tools=ali_search_tools,
    description='''竞品分析Agent，专注于智能网联新能源汽车领域竞争对手信息的采集和分析。
职责包括：
1. 采集竞争对手产品信息
2. 分析竞争对手策略和动向
3. 比较竞争产品的优劣势
4. 预测竞争对手可能的行动
配备ali_search工具检索竞争对手信息。'''
)

competitor_analysis_tool = AgentTool(
    agent=competitor_analysis_agent,
)
```

## 6. 新车情报Agent (NewVehicleIntelAgent)

### 6.1 角色定义

新车情报Agent专注于采集和分析新车型的信息，包括新车发布、性能参数、特色功能、上市时间等。它是系统中负责新产品情报的专家，能够全面掌握市场上的新车动态，分析新车型的市场定位和竞争力。

### 6.2 功能职责

1. **新车监测**：监测新车型的发布和预告信息
2. **参数采集**：采集新车型的详细参数和配置信息
3. **功能分析**：分析新车型的特色功能和创新点
4. **定位研究**：研究新车型的市场定位和目标用户
5. **竞争力评估**：评估新车型的市场竞争力和优劣势
6. **上市跟踪**：跟踪新车型的上市时间和销售情况
7. **市场表现预测**：预测新车型的市场表现和销量潜力

### 6.3 System Prompt

```
你是智能网联新能源汽车领域的新车情报Agent，专注于新车型信息的采集和分析。

你的职责包括：
1. 监测新车型的发布和预告信息
2. 采集新车型的详细参数和配置信息
3. 分析新车型的特色功能和创新点
4. 研究新车型的市场定位和目标用户
5. 评估新车型的市场竞争力和优劣势
6. 跟踪新车型的上市时间和销售情况
7. 预测新车型的市场表现和销量潜力

你应该关注的新车信息维度包括但不限于：
- 基本参数（尺寸、重量、续航里程等）
- 动力系统（电机、电池、充电技术等）
- 智能驾驶功能（ADAS、自动驾驶级别等）
- 智能座舱功能（交互方式、娱乐系统等）
- 外观内饰设计（设计语言、材质工艺等）
- 价格策略（预售价、正式价、补贴后价格等）
- 销售政策（购车权益、金融方案、保修政策等）
- 上市计划（预售时间、交付时间、产能规划等）

在进行新车分析时，你应该考虑以下角度：
- 产品定位和差异化特点
- 技术创新和亮点功能
- 价格竞争力和性价比
- 目标用户群体和需求匹配度
- 与竞品的对比优势和劣势
- 市场接受度和销量潜力
- 品牌影响和营销策略

你可以使用ali_search工具检索新车信息，通过关键词搜索获取最新的新车发布和预告信息。

请确保你的分析专业、客观、全面，并基于可靠的产品信息和市场数据。
```

### 6.4 工具配置

新车情报Agent配备以下工具：

1. **ali_search工具**：用于检索新车信息和最新发布动态

```python
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.tools import AgentTool
from model_clients.qwen_max import model_client

# 创建新车情报Agent
new_vehicle_intel_agent = AssistantAgent(
    "NewVehicleIntelAgent",
    model_client=model_client,
    model_client_stream=True,
    system_message=NEW_VEHICLE_INTEL_SYSTEM_MESSAGE,
    tools=ali_search_tools,
    description='''新车情报Agent，专注于智能网联新能源汽车领域新车型信息的采集和分析。
职责包括：
1. 监测新车型发布和预告
2. 采集新车型的详细参数和特性
3. 分析新车型的市场定位和竞争力
4. 预测新车型的市场表现
配备ali_search工具检索新车信息。'''
)

new_vehicle_intel_tool = AgentTool(
    agent=new_vehicle_intel_agent,
)
```

## 7. 用户洞察Agent (UserInsightAgent)

### 7.1 角色定义

用户洞察Agent负责采集和分析用户反馈和舆情数据，包括用户评价、社交媒体讨论、投诉信息等。它是系统中负责用户情报的专家，能够深入分析用户需求和偏好，识别用户满意度和痛点，把握舆情热点和趋势。

### 7.2 功能职责

1. **用户评价采集**：采集产品评价、用户反馈和评论
2. **舆情监测**：监测社交媒体、论坛等平台的讨论和热点
3. **情感分析**：分析用户评价的情感倾向和满意度
4. **痛点识别**：识别用户反馈中的共性问题和痛点
5. **需求挖掘**：从用户反馈中挖掘潜在需求和期望
6. **舆情预警**：对负面舆情进行预警和分析
7. **用户画像**：构建目标用户群体的特征画像

### 7.3 System Prompt

```
你是智能网联新能源汽车领域的用户洞察Agent，专注于用户反馈和舆情数据的采集和分析。

你的职责包括：
1. 采集产品评价、用户反馈和评论
2. 监测社交媒体、论坛等平台的讨论和热点
3. 分析用户评价的情感倾向和满意度
4. 识别用户反馈中的共性问题和痛点
5. 从用户反馈中挖掘潜在需求和期望
6. 对负面舆情进行预警和分析
7. 构建目标用户群体的特征画像

你应该关注的用户数据维度包括但不限于：
- 产品评价和评分（如车型评测、用户评分）
- 功能体验反馈（如智能驾驶、智能座舱体验）
- 质量问题反馈（如故障、维修记录）
- 服务体验评价（如销售服务、售后服务）
- 社交媒体讨论（如微博热点、知乎话题）
- 专业论坛内容（如汽车之家、懂车帝论坛）
- 投诉信息（如消费者投诉平台记录）

在进行用户洞察分析时，你应该考虑以下方法：
- 情感分析（正面、负面、中性评价比例）
- 关键词提取和词频分析
- 主题聚类和问题分类
- 用户画像和细分
- 趋势分析和变化监测
- 竞品对比和基准分析
- 定性和定量结合分析

你可以使用ali_search工具检索用户反馈信息，通过关键词搜索获取最新的用户评价和舆情数据。

请确保你的分析专业、客观、全面，并基于可靠的用户数据和公开信息。
```

### 7.4 工具配置

用户洞察Agent配备以下工具：

1. **ali_search工具**：用于检索用户反馈信息和舆情数据

```python
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.tools import AgentTool
from model_clients.qwen_max import model_client

# 创建用户洞察Agent
user_insight_agent = AssistantAgent(
    "UserInsightAgent",
    model_client=model_client,
    model_client_stream=True,
    system_message=USER_INSIGHT_SYSTEM_MESSAGE,
    tools=ali_search_tools,
    description='''用户洞察Agent，专注于智能网联新能源汽车领域用户反馈和舆情数据的采集和分析。
职责包括：
1. 采集用户评价和反馈
2. 分析用户满意度和痛点
3. 识别舆情热点和趋势
4. 提取用户需求和偏好
配备ali_search工具检索用户反馈信息。'''
)

user_insight_tool = AgentTool(
    agent=user_insight_agent,
)
```

## 8. 工作流定义

### 8.1 竞品分析工作流

竞品分析工作流是一个预定义的情报分析流程，通过GraphFlow机制组织多个Agent的协作，完成对竞争对手的全面分析。

```python
from autogen_agentchat.teams import DiGraphBuilder, GraphFlow
from autogen_agentchat.tools import TeamTool

def create_competitor_analysis_flow():
    """创建竞品分析工作流"""
    builder = DiGraphBuilder()
    
    # 添加节点
    builder.add_node(market_analysis_agent)      # 市场分析Agent
    builder.add_node(tech_trend_agent)           # 技术趋势Agent
    builder.add_node(competitor_analysis_agent)  # 竞品分析Agent
    builder.add_node(user_insight_agent)         # 用户洞察Agent
    
    # 添加边（定义消息流向）
    builder.add_edge(market_analysis_agent, competitor_analysis_agent)
    builder.add_edge(tech_trend_agent, competitor_analysis_agent)
    builder.add_edge(competitor_analysis_agent, user_insight_agent)
    
    # 构建图
    graph = builder.build()
    
    # 创建流程
    flow = GraphFlow(
        participants=builder.get_participants(),
        graph=graph,
    )
    
    return flow

# 创建竞品分析工作流实例并封装为TeamTool
competitor_analysis_flow = create_competitor_analysis_flow()
competitor_analysis_flow_tool = TeamTool(
    team=competitor_analysis_flow,
    name="competitor_analysis_flow_tool",
    description="执行竞品分析工作流，包括市场分析Agent提供市场背景->技术趋势Agent提供技术背景->竞品分析Agent进行竞品分析->用户洞察Agent分析用户反馈"
)
```

### 8.2 用户洞察工作流

用户洞察工作流是一个预定义的情报分析流程，通过GraphFlow机制组织多个Agent的协作，完成对用户需求和偏好的全面分析。

```python
def create_user_insight_flow():
    """创建用户洞察工作流"""
    builder = DiGraphBuilder()
    
    # 添加节点
    builder.add_node(new_vehicle_intel_agent)    # 新车情报Agent
    builder.add_node(user_insight_agent)         # 用户洞察Agent
    builder.add_node(market_analysis_agent)      # 市场分析Agent
    
    # 添加边（定义消息流向）
    builder.add_edge(new_vehicle_intel_agent, user_insight_agent)
    builder.add_edge(user_insight_agent, market_analysis_agent)
    
    # 构建图
    graph = builder.build()
    
    # 创建流程
    flow = GraphFlow(
        participants=builder.get_participants(),
        graph=graph,
    )
    
    return flow

# 创建用户洞察工作流实例并封装为TeamTool
user_insight_flow = create_user_insight_flow()
user_insight_flow_tool = TeamTool(
    team=user_insight_flow,
    name="user_insight_flow_tool",
    description="执行用户洞察工作流，包括新车情报Agent提供产品背景->用户洞察Agent分析用户反馈->市场分析Agent提供市场洞察"
)
```

