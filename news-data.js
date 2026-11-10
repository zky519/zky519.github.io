window.NEWS_DATA = {
  "updatedAt": "2026-11-10T16:45:35+08:00",
  "reportDate": "2026-11-10",
  "items": [
    {
      "title": "Anthropic 发布 Claude Fable 5.2 与 Mythos 5.2",
      "summary": "Anthropic于11月9日发布Claude Fable 5.2和Mythos 5.2，面向复杂编码、推理、视觉和科研任务。两者采用相同底层模型，但Fable加入网络安全及生物安全防护，可更广泛提供；Mythos面向通过验证的相关研究机构。官方公布标准价格为每百万输入token 8美元、输出40美元，并称生成速度较5.1最高提升30%；另有价格更高的快速模式。这些效果属于厂商测试结果。此次更新值得关注的既有高难度任务能力，也有速度与价格变化，实际使用仍应按自身任务比较质量和总成本。",
      "category": "AI行业",
      "source": "Anthropic",
      "url": "https://www.anthropic.com/claude-fable-and-mythos-5-2",
      "publishedAt": "2026-11-09",
      "context": "影响开发者模型选型。",
      "verification": "official"
    },
    {
      "title": "Google 扩充 TPU 产品线",
      "summary": "Google于11月9日公布TPU 8tx与TPU 8i Max，将第八代产品组合扩展为四种系统。8tx主要面向敏感数据和受监管行业的机密推理，配合AMD EPYC主机，在数据使用期间保护数据和模型权重。8i Max把两颗8i芯片放入同一封装，官方称计算、片上SRAM和高带宽内存带宽均翻倍，针对超长上下文与多agent工作负载。Google强调这属于围绕既有芯片调整封装、网络、内存与安全的系统创新。对基础设施选型而言，重点从单颗芯片性能扩展到了整机密度、内存瓶颈和安全能力。",
      "category": "AI行业",
      "source": "Google",
      "url": "https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/",
      "publishedAt": "2026-11-09",
      "context": "AI 算力供应竞争持续。",
      "verification": "official"
    },
    {
      "title": "Meta 推出 Muse Ember",
      "summary": "Meta于11月9日推出Muse Ember，定位为处理工具调用、编码子任务、路由、信息抽取和长文档解析的轻量模型。官方介绍其拥有100万token上下文窗口，可将代码库或文档集合放进一次请求，并原生处理文本、图像、音频和视频。Meta Model API公布价格为每百万输入token 0.10美元、输出0.50美元。Meta展示了业务流程、编码和计算机使用测试，但这些比较仍应视作发布方公布的评测。它的重要性在于降低大量重复agent步骤的成本，使高端模型负责难题、轻量模型承担日常执行的组合更值得尝试。",
      "category": "AI行业",
      "source": "Meta",
      "url": "https://research.meta.ai/blog/muse-ember",
      "publishedAt": "2026-11-09",
      "context": "值得关注 agent 推理成本。",
      "verification": "official"
    },
    {
      "title": "NVIDIA 在 CoRL 展示机器人训练技术",
      "summary": "NVIDIA在11月9日的CoRL发布中介绍GR00T 2、Isaac Lab 3.0及工业机器人评测工具，重点从移动能力转向接线、装配和灵巧操作。Isaac Lab 3.0可在PhysX与Newton物理求解器之间切换，支持柔性物体和机器人手部等复杂系统；研究者可先在大量并行仿真环境中训练，再向真实机器人迁移。发布内容还包括面向工业场景的DexBench与VABAR，帮助比较不同物体、空间和物理条件下的表现。对于具身智能行业，这些工具的价值在于完善数据、训练和评估链条，而不仅是发布一个新的机器人模型。",
      "category": "AI行业",
      "source": "NVIDIA",
      "url": "https://blogs.nvidia.com/blog/robotics-simulation-advancements-corl/",
      "publishedAt": "2026-11-09",
      "context": "具身智能工具链继续扩展。",
      "verification": "official"
    },
    {
      "title": "Google推出TPU agent suite预览，降低算力开发门槛",
      "summary": "在11月9日的基础设施发布中，Google同时介绍了处于预览阶段的开源TPU agent suite。该工具可接入Claude Code、Cursor等编码环境，通过自然语言协助开发者完成TPU入门、诊断性能瓶颈以及自动调优自定义内核。Google还回顾了此前开源的TorchTPU，使PyTorch代码和Hugging Face模型可以在TPU上原生运行，并提及vLLM、SGLang的TPU后端支持。这条动态关注软件使用门槛，与同日发布的TPU硬件系统相互配合。对于已有GPU工作流的团队，工具链兼容性和迁移成本通常与硬件指标同样重要；预览功能的适用范围应以文档为准。",
      "category": "AI行业",
      "source": "Google",
      "url": "https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/",
      "publishedAt": "2026-11-09",
      "context": "AI基础设施的软件生态与迁移成本。",
      "verification": "official"
    },
    {
      "title": "中国前十个月外贸同比增长20%",
      "summary": "新华社11月10日引述海关总署数据报道，今年前10个月中国货物贸易进出口总值44.81万亿元，同比增长20%；10月单月进出口4.87万亿元，同比增长31.2%。累计出口25.99万亿元、增长17.6%，进口18.82万亿元、增长23.6%。机电产品占出口比重达到64.7%，进口增速快于出口。报道将外贸增长与市场多元化、产业结构升级等因素联系起来。阅读这组数据时，需要区分人民币计价的贸易金额变化与实际货运数量变化；对宏观观察而言，它提供了外需、进口需求和制造业出口结构的最新线索。",
      "category": "政治经济",
      "source": "新华网",
      "url": "https://www.news.cn/fortune/20261110/9afec94b24df4805b3d8797a5d884bf3/c.html",
      "publishedAt": "2026-11-10T14:12:55+08:00",
      "context": "观察外需与贸易韧性。",
      "verification": "reported"
    },
    {
      "title": "中国10月CPI同比上涨0.7%",
      "summary": "据人民日报海外版11月10日报道，国家统计局11月9日公布的10月CPI同比上涨0.7%，环比持平；核心CPI同比上涨0.8%，两项同比涨幅均较上月回落0.2个百分点。同期PPI同比上涨5.7%，环比上涨0.7%。食品价格下降与能源相关行业价格上涨同时存在，说明消费端与工业上游的价格表现并不一致。报道还指出，国际能源价格及季节性需求影响部分工业品价格。观察物价时，既要看总体CPI，也要看核心指标和生产端价格，不能将单一指数变化直接等同于所有行业需求同步改善。",
      "category": "政治经济",
      "source": "人民日报海外版／新华网",
      "url": "https://www.news.cn/fortune/20261110/830b78c183f7453792f834a0289e1463/c.html",
      "publishedAt": "2026-11-10T07:54:06+08:00",
      "context": "反映消费价格变化。",
      "verification": "reported"
    },
    {
      "title": "法国政府与劳资代表展开社会对话",
      "summary": "据世界报11月9日报道，法国总理勒科尔尼安排与企业和工会代表举行社会会议，并在当周与学生及公务员代表交流。背景是围绕生活成本、薪资和教育条件持续出现的抗议，最低工资调整是劳资讨论的重要议题。报道显示，政府试图通过社会对话回应民生诉求，同时面临就业和财政约束。该报道描述的是会谈安排与政策分歧，没有宣布已达成加薪协议。后续应关注政府提出的具体措施，以及工会和企业的回应。",
      "category": "政治经济",
      "source": "Le Monde",
      "url": "https://www.lemonde.fr/en/politics/article/2026/11/09/french-pm-hosts-union-and-business-representatives-to-kick-off-week-of-high-stakes-talks_6775705_5.html",
      "publishedAt": "2026-11-09",
      "context": "关注民生压力与政策回应。",
      "verification": "reported"
    },
    {
      "title": "欧洲多国出现数据中心抗议活动",
      "summary": "世界报11月9日报道，欧洲约15个国家在前一周末出现反对大型数据中心建设的活动，组织方要求暂停扩张并加强公共讨论。抗议涉及用水、电力消耗、噪声及当地环境影响，法国、西班牙、英国等地均有活动。这是对数据中心建设的社会反应，并不代表欧洲政府已统一暂停项目。对AI基础设施投资而言，土地和设备之外，地方支持、资源使用透明度及能源供给也是需要解决的条件。报道日期为11月9日，活动发生在此前周末。",
      "category": "政治经济",
      "source": "Le Monde",
      "url": "https://www.lemonde.fr/en/economy/article/2026/11/09/protests-against-data-centers-held-across-europe_6775706_19.html",
      "publishedAt": "2026-11-09",
      "context": "AI 投资面临地方资源约束；事件早于24小时窗口。",
      "verification": "reported"
    },
    {
      "title": "宁波舟山港年集装箱吞吐量突破4000万标准箱",
      "summary": "新华社11月10日报道，截至当日，宁波舟山港今年集装箱吞吐量超过4000万标准箱，连续第二年达到该水平，比去年提前22天。港口目前拥有115条海铁联运线路，覆盖16个省份、71个地级市，集装箱航线超过310条，连接全球700多个港口。报道还提及中欧北极快航在通航季完成8个航次。吞吐量增长体现物流通道的作业规模，而航线和内陆联运网络决定货物组织效率。对外贸企业而言，港口能力、运输时间和通道稳定性影响交货安排；港口吞吐量也不能简单等同于全国出口额的增长速度。",
      "category": "政治经济",
      "source": "新华网",
      "url": "https://www.news.cn/fortune/20261110/d007347efa3f46a2b8bc09f5bc744381/c.html",
      "publishedAt": "2026-11-10T15:34:47+08:00",
      "context": "观察外贸物流和港口通道能力。",
      "verification": "reported"
    },
    {
      "title": "《欧洲卡车模拟2》冰岛DLC",
      "summary": "PC Gamer的11月发售日历将《欧洲卡车模拟2》冰岛DLC列在11月10日，作为本日的驾驶模拟扩展提醒。对已经拥有本体、喜欢公路运输与沿途风景的玩家，这条信息的重点是新增地区内容，而非一款独立续作。媒体将其作为当月值得关注的扩展之一。本条按日历计划介绍，不把日期自动等同于所有地区已同时解锁，也不添加来源未提供的道路规模、售价或性能结论。阅读时可先判断自己是否希望继续扩充驾驶地图；购买所需的本体条件和具体版本信息以发行页面为准。",
      "category": "单机游戏",
      "source": "PC Gamer",
      "url": "https://www.pcgamer.com/games/november-games-2026/",
      "publishedAt": "2026-11-04T23:37:01Z",
      "context": "近日单人游戏发行计划提醒。",
      "verification": "media_calendar"
    },
    {
      "title": "《Monster Train 2》The Punished DLC",
      "summary": "PC Gamer的11月日历将《Monster Train 2》扩展The Punished列于11月10日，并介绍其新增一个派系。对于关注单人卡牌策略的玩家，新增派系的意义通常在于提供不同的构筑方向和组合空间；本条不把这一一般性观察当成游戏平衡或质量结论。媒体将其列入当月DLC亮点，因此作为今日扩展提醒收入日报。这里所述为媒体明确列出的计划，不额外断言所有平台已经开放下载，也不补写未经来源支持的卡牌数量、售价和折扣。已有本体的玩家可将它作为后续体验新构筑的关注项。",
      "category": "单机游戏",
      "source": "PC Gamer",
      "url": "https://www.pcgamer.com/games/november-games-2026/",
      "publishedAt": "2026-11-04T23:37:01Z",
      "context": "近日单人游戏发行计划提醒。",
      "verification": "media_calendar"
    },
    {
      "title": "《Warhammer Survivors》",
      "summary": "PC Gamer在11月发售日历中将《Warhammer Survivors》列为11月10日的新作；其年度游戏介绍将它描述为Auroch Digital与《吸血鬼幸存者》团队合作的弹幕生存作品。本条作为今日发行计划提醒，面向喜欢单局成长和生存动作玩法的读者。仅凭发售日历不能推导最终口碑、内容时长或性能表现，因此摘要不作这些承诺。与多人赛季更新相比，这类新作更适合按作品本身的玩法和题材判断是否关注；日期按媒体日历表述，具体地区的开放时间应以发行方页面为准。",
      "category": "单机游戏",
      "source": "PC Gamer",
      "url": "https://www.pcgamer.com/games/november-games-2026/",
      "publishedAt": "2026-11-04T23:37:01Z",
      "context": "近日单人游戏发行计划提醒。",
      "verification": "media_calendar"
    },
    {
      "title": "《Ashes of the Singularity 2》",
      "summary": "PC Gamer将《Ashes of the Singularity 2》列入11月10日发售日历，并在年度新作介绍中将其归为科幻即时战略续作。对于关注单机策略游戏的读者，它是一条值得记下的新作计划，而非评测推荐或已验证的品质判断。现有报道能够支持名称、类型与日历日期，不能据此增加阵营数量、战役长度、引擎性能或硬件要求等细节。本条据媒体日历提供清晰的时间提醒，避免将平台解锁状态写成确定事实。读者可结合自己对即时战略的兴趣决定是否继续关注后续正式评测。",
      "category": "单机游戏",
      "source": "PC Gamer",
      "url": "https://www.pcgamer.com/games/november-games-2026/",
      "publishedAt": "2026-11-04T23:37:01Z",
      "context": "近日单人游戏发行计划提醒。",
      "verification": "media_calendar"
    },
    {
      "title": "《Dreadmoor》抢先体验",
      "summary": "PC Gamer的11月重点推荐将《Dreadmoor》列在11月9日，并以恐怖氛围中的钓鱼体验介绍其抢先体验计划。它的吸引点在于将水域探索与惊悚感结合，而本次上线形态为抢先体验，不应与内容已完整的正式版混为一谈。本条作为近日发行提醒纳入今日整理，来源报道早于今天，计划日期明确写为11月9日。摘要不把媒体编辑的期待当成最终评测，也不补写价格、完成度或后续开发承诺。对喜欢恐怖探索的玩家，是否接受抢先体验阶段的内容变化，是判断这条资讯相关性的主要因素。",
      "category": "单机游戏",
      "source": "PC Gamer",
      "url": "https://www.pcgamer.com/games/november-games-2026/",
      "publishedAt": "2026-11-04T23:37:01Z",
      "context": "近日单人游戏发行计划提醒。",
      "verification": "media_calendar"
    },
    {
      "title": "圣保罗站：Norris 夺冠",
      "summary": "F1官方成绩表显示，11月8日圣保罗大奖赛正赛由McLaren车手Lando Norris获胜，完成71圈，用时1小时35分23.504秒。Red Bull车手Max Verstappen落后14.602秒获得第二，Isack Hadjar位列第三。Mercedes的George Russell和Kimi Antonelli分列第四、第五；Oscar Piastri第六，Charles Leclerc与Lewis Hamilton分别第八、第九。官方结果页还列明部分车手的赛后处罚，日报采用结果表最终顺序。本条属于近三天赛事回顾，并非11月10日新举行的比赛，为读者提供直接可读的主要赛果。",
      "category": "F1",
      "source": "Formula 1",
      "url": "https://www.formula1.com/en/results/2026/races/1299/brazil/race-result",
      "publishedAt": "2026-11-08",
      "context": "近72小时赛果回顾。",
      "verification": "official"
    },
    {
      "title": "Mercedes在圣保罗锁定车队冠军，雨战轮胎策略左右比赛",
      "summary": "轮胎供应商Pirelli在11月8日赛后报告中确认，Russell和Antonelli以第四、第五名完赛，帮助Mercedes获得足够积分锁定车队年度冠军。比赛起步时赛道湿滑，所有车手使用半雨胎，随后转为软胎；Norris等领先车手在末段降雨后重新换回半雨胎。Pirelli介绍，Russell和Leclerc曾在同一套软胎上完成45圈，反映不同车手对天气和轮胎寿命采取了不同策略。本条以车队冠军与策略为重点，与单纯赛果分别呈现；这是11月8日的赛后信息，纳入近三天回顾。",
      "category": "F1",
      "source": "Pirelli",
      "url": "https://press.pirelli.com/from-pole-to-victory-norris-triumphs-in-so-paulo-on-intermediates/",
      "publishedAt": "2026-11-08T22:31:00+01:00",
      "context": "车队冠军归属与雨战策略。",
      "verification": "official"
    }
  ],
  "revision": 2,
  "notice": "本期 17 条 · 新闻由采集模块核实与编辑 · 游戏保留发售计划口径，赛事保留回顾日期。"
};
