---
name: voc-momcozy-e2e
description: Momcozy喂养电器全链路E2E洞察项目工作目录。涵盖VOC分析报告生成、ECharts可视化、HTML报告构建与修复脚本、AI Agent记忆系统。当在此目录工作时使用。
---

# VOC - Momcozy喂养电器 E2E洞察项目

**Generated:** 2026-05-20  
**项目状态:** 活跃 - V5已完成，全站ECharts规范化完成，腾讯云独立部署上线（2026-05-27）

## 概览

Momcozy喂养电器品牌营销/产品洞察工作区。核心产出是多版本HTML洞察报告（ECharts可视化），数据基座为六源交叉验证（Amazon VOC 19,098条 + Meta社媒 + Meltwater 75,291条 + 经营数据 + 市场研究 + 竞品VOC）。

## 网站

**GitHub Pages**: https://zjgulai.github.io/VOC/  
**腾讯云独立部署**: https://report.lute-tlz-dddd.top （2026-05-27上线，Nginx静态托管）  
**仓库**: https://github.com/zjgulai/VOC.git

## 目录结构

```
VOC/
├── docs/               # GitHub Pages部署目录 - 多页面网站
│   ├── index.html      # 报告库首页
│   ├── strategy.html   # 策略与洞察
│   ├── product.html    # 产品与定义
│   ├── execution.html  # 落地与执行
│   ├── methodology.html# 工作流方法论
│   └── reports/        # 子页面报告（e2e-v5.html + stage1-7）
├── html_report/        # 主报告输出 - V5.html等
├── data/
│   ├── voc/            # Amazon VOC原始数据（xlsx/csv）
│   └── vos/            # 社媒数据（FB/IG，xlsx/csv，按年份编号）
├── script/             # Python修复/合并脚本
├── memory_chat/        # Agent记忆系统（MEMORY.md为主记录）
├── imgs/               # AI生成产品图（按批次日期分组）
└── video/              # Final Cut Pro项目（.fcpxml + MP4/MP3素材）
```

## 当前主要文件

| 文件 | 说明 |
|------|------|
| `html_report/VOC喂养电器E2E洞察报告_V5.html` | **主报告** 9680行/34 sections，含前置洞察10章节+E2E执行模块 |
| `html_report/report_data.json` | ECharts图表数据源 |
| `memory_chat/MEMORY.md` | **必读** - 完整任务状态、Workflow进度、数据源路径 |
| `memory_chat/TOOLS.md` | ECharts规范、大文件处理、子session管理规则 |
| `memory_chat/USER.md` | 用户偏好、报告规范要求、审美标准 |

## 关键技术规范（必须遵守）

### ECharts防溢出规范
```javascript
grid: {left:80, right:40, top:60, bottom:80}
axisLabel: {rotate:30, fontSize:11, overflow:'truncate', width:80}
tooltip: {confine:true}
// radar: radius:'65%'  pie: radius:['35%','65%']
// pie: avoidLabelOverlap:true, legend:{type:'scroll',bottom:0}, label.show:false
// radar trigger: 'item' (不是 'axis')
// ECharts5 radar: axisName:{} (废弃字段 name:{})
```

### 新增图表必须
1. 新增 `<div id="chart-xxx">` 对应新增 `function initXxxChart()`
2. 在 `initAllCharts()` 中用 `safeInit('chart-xxx', initXxxChart)` 包裹调用
3. 遵循 Fortune Red 色卡：`#D75B70`主 / `#F37969`辅 / `#D0B671`金 / `#82AE8E`绿 / `#C1CEDE`灰 / `#6A89AF`蓝

### 导航栏规范
全站统一单行导航栏，V5报告 + `docs/` 5页面对齐：
```css
.nav-bar { height: 44px; position: sticky; top: 0; background: rgba(255,255,255,0.97); backdrop-filter: blur(12px); border-bottom: 2px solid var(--fr-300); }
.nav-title { font-size: 13px; border-right: 2px solid var(--fr-300); padding-right: 16px; }
.nav-link { font-size: 12px; color: var(--fr-800); opacity: 0.7; }
.nav-link:hover, .nav-link.active { background: rgba(215,91,112,0.12); color: var(--fr-600); opacity: 1; }
```

### 报告内容规范
- 每模块末尾必须有**【结论句】**，一句话回答核心问题
- 禁止"可能""或许"等模糊措辞；无数据支撑标注`【推断：需XX数据验证】`
- 标题和表格禁用 emoji，用品类色胶囊替代
- 不删除/替换原有图表（除非明确说明）

### HTML大文件修复流程
```
提取HTML → 修复重复ID → 重写JS → 组装文件
验证：node --check 语法检查 → grep -c "initChart" 匹配div:init=1:1 → wc -l 行数确认
```

### CDN注入（Coze环境限制）
静态 `<script>` 标签被阻断，必须用 `document.createElement('script')` 动态注入，三源 fallback：jsdelivr → unpkg → cdnjs

## 数据源路径（V5对应）

| 代号 | 描述 | 路径 |
|------|------|------|
| D1 | Amazon VOC 19,098条 | `data/voc/VOC_喂养电器_打标明细_2026-05-13_*.xlsx` |
| D2 | Meta社媒 2,238条 | `data/vos/FB/` + `data/vos/IG/` |
| D3 | Meltwater全网 75,291条 | `html_report/` 中对应MD |
| D4 | 经营数据 | `data/voc/meltwater_voc_clean.csv` |
| D5 | 外部市场研究 | html_report MD文件 |
| D6 | 竞品VOC 54,189条 | html_report MD文件 |

## Workflow完成状态（截至V5）

所有 WF01-WF08 ✅，社媒画像扩展 ✅，Meltwater整合 ✅，六源矛盾确认 ✅，E2E V3/V4/V5重构 ✅

详细状态见 `memory_chat/MEMORY.md`。

## 常用操作

```bash
# 验证HTML语法
node --check html_report/VOC喂养电器E2E洞察报告_V5.html

# 检查chart div与initChart函数数量是否1:1
grep -c 'id="chart-' html_report/VOC喂养电器E2E洞察报告_V5.html
grep -c 'initChart\|function init' html_report/VOC喂养电器E2E洞察报告_V5.html

# 查看文件大小
wc -l html_report/VOC喂养电器E2E洞察报告_V5.html

# 运行修复脚本（需先确认输入路径存在）
python3 script/fix_voc_report.py
python3 script/merge_report.py
```

## 注意事项

- **有 git 仓库** - 推送到 https://github.com/zjgulai/VOC.git，`docs/` 目录由 GitHub Pages 部署
- **腾讯云部署** - `report.lute-tlz-dddd.top` 静态文件在 `/opt/voc-report/html/`，nginx 配置在 `/opt/ai-video/deploy/lighthouse/`；更新内容只需 `rsync docs/ ubuntu@101.34.52.232:/opt/voc-report/html/`，无需重启容器
- **服务器 SSH** - `ssh -i /Users/lute/project/VOA/VOC/ai_video.pem ubuntu@101.34.52.232`
- **本地预览** - `python3 -m http.server 8765` 启动后访问 `http://localhost:8765/docs/`
- **导航栏规范** - 单行44px + sticky定位 + brand竖线分隔，与V5主报告对齐（见下方CSS）
- **大文件处理** - V5报告9680行，修改前用 `grep -n` 定位目标行，分块操作避免覆盖
- **子session命名** - 大规模重构（8000+行）派发子session，任务描述需含完整修改清单+输出路径+自验证清单
- **Sankey图禁用** - 节点名必须唯一且双向流导致空白，改用HTML/CSS卡片替代
- **文件路径** - 脚本中使用绝对路径；`用户上传/` 路径为历史遗留，当前主路径为 `html_report/`
- **用户偏好** - 简洁高效，不需要关怀性收尾；截图反馈UI问题时精准修复，不扩大范围
