# 新闻数据接入

无需改动页面，只更新根目录 news-data.js：

```js
window.NEWS_DATA = {
  updatedAt: "2026-11-10T08:00:00+08:00",
  items: [{
    title: "新闻标题",
    summary: "简短摘要",
    category: "科技",
    source: "来源名称",
    publishedAt: "2026-11-10T07:30:00+08:00",
    url: "https://example.com/news"
  }]
};
```

分类：国内、国际、科技、AI。页面按数组顺序展示。日期使用 ISO 8601 格式。
抓取、调度、来源授权与内容质量由新闻模块维护。本页面不抓取新闻。
数据为公开内容，不得写入密钥。使用 JSON.stringify 序列化对象生成 JS 数据，避免拼接未转义文本。
GitHub Pages 若使用 main 分支根目录发布，提交文件即可触发更新。
