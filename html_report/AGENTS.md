---
name: voc-html-report
description: VOC洞察报告主输出目录，含所有HTML报告版本、ECharts数据源、叙事逻辑MD文档。
---

# html_report/ - 报告输出目录

## 文件清单

| 文件 | 状态 | 说明 |
|------|------|------|
| `VOC喂养电器E2E洞察报告_V5.html` | **当前主版本** | 9680行，34 sections，~593KB |
| `VOC喂养电器E2E洞察报告_V4.html` | 历史版 | V4修正版 |
| `VOC喂养电器E2E洞察报告_V3.html` | 历史版 | V3重构版 |
| `report_data.json` | 数据源 | ECharts图表数据 |
| `E2E报告叙事逻辑.md` | 叙事架构 | 11模块叙事结构说明 |
| `E2E叙事逻辑V3终版.md` | 叙事架构 | V3最终叙事逻辑 |
| `六源整合与矛盾确认清单.md` | 数据质量 | 逐结论标注D1-D6来源，10项矛盾+15项新增块 |
| `_echarts_test.html` | 测试文件 | ECharts组件测试用 |
| `temp_body.html` / `temp_header.html` | 临时文件 | 大文件分块操作的中间产物，可删 |

## 修改大文件的安全流程

```bash
# 1. 定位目标行（不要全文读取）
grep -n 'chart-xxx\|target-section' VOC喂养电器E2E洞察报告_V5.html

# 2. 语法验证（修改后必做）
node --check VOC喂养电器E2E洞察报告_V5.html

# 3. chart div与init函数1:1验证
grep -c 'id="chart-' VOC喂养电器E2E洞察报告_V5.html
grep -c 'safeInit(' VOC喂养电器E2E洞察报告_V5.html
# 两数必须相等

# 4. 行数确认
wc -l VOC喂养电器E2E洞察报告_V5.html
```

## 报告内部结构（V5）

- **导航栏**：单行44px sticky，`nav-title` 竖线分隔，`nav-link` 深色 opacity 0.7。与 `docs/` 首页导航完全对齐
- **导航分组**：【前置洞察】（10章节）+ 【E2E执行】【用户深潜】【机会提炼】【上市落地】
- **图表数量**：当前约80个 chart div，对应等量 safeInit 调用
- **JS结构**：所有图表通过 `safeInit('chart-id', initFn)` 在 `initAllCharts()` 中统一初始化

## 禁止操作

- **禁止删除原有图表**（除非用户明确指示）
- **禁止 Sankey 图**（节点名唯一性+双向流问题导致空白）
- **禁止直接覆盖写大文件**——必须先 grep 定位，再分块 Edit
