---
title: "Personal Blog"
date: 2021-03-06T16:27:28-08:00
draft: false
toc: true
images:
tags:
  - intro
---

# Overview
This is personal blog power by hugo hosted on github pages

# Setup procedure

On MacBook install `hugo`

```bash
brew install hugo
```

Create a new site
```bash
hugo new site [project-name]
```

Choose a theme

we can either git clone or git submodule, since we might want to customize the theme later on, we choose to git clone

```bash
git clone https://github.com/rhazdon/hugo-theme-hello-friend-ng.git themes/hello-friend-ng
mv themes/hello-friend-ng/exampleSite/* ./
rm content/posts/*
```

Create a new post
```
hugo new posts/my-first-post.md
```


## Reference
- https://gohugo.io/getting-started/quick-start/
- https://zhuanlan.zhihu.com/p/126298572
- https://zhangfelix.medium.com/%E4%BD%BF%E7%94%A8hugo%E5%92%8Cgithub%E6%90%AD%E5%BB%BA%E5%8D%9A%E5%AE%A2-cbd1d57fcfbf
- https://github.com/rhazdon/hugo-theme-hello-friend-ng