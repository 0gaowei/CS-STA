# 计科协开源学习项目计划

## 项目介绍

本项目由西安电子科技大学计科协（CS-STA）发起，旨在提供一个开源学习资源库和开源项目库，涵盖多个技术方向，包括但不限于ACM、数模、AI、Web、CTF、嵌入式等。通过参与本项目，成员可以快速入门各个技术方向，参与开源项目的二次开发，并有机会参加各类竞赛。

### 各个方向负责人

- acm：[Verkundet](https://github.com/Verkundet)
- 数模：[0gaowei](https://github.com/0gaowei)
- ai：[sagarua](https://github.com/sagarua99)
- 开发：[Sam-D709](https://github.com/Sam-D709)
- 嵌入式：[Kyle](https://github.com/Kyle0466)
- CTF：[Westle](https://github.com/Westle2)

### 项目目标

- 快速入门：通过组长引导，快速学习各个方向的知识，解决入门迷茫问题。
- 开源贡献：参与学习资源的开源共享，提升专业能力和沟通能力。
- 项目开发：直接参与开源项目开发，积累项目经验。
- 竞赛准备：通过项目开发，为参加各类竞赛做好准备。

### 项目路线

1. 各方向入门学习：通过组长引导，快速入门各个技术方向。
2. 开源项目二次开发：参与开源项目的二次开发，积累项目经验。
3. 参加各类竞赛：通过项目开发，为参加各类竞赛做好准备。

### 组织架构

- 每个方向有一个组长，负责提供学习方向与资源，审核他人提供的资源，管理GitHub上对应的仓库，并主持交流会。
- CSSTA组员与社区成员可以学习某个方向的知识，完成组长布置的任务，提供优质的学习资源，并在GitHub上发起`PR` 请求。小组成员每周汇报进度，可以咨询组长问题，由组长进行答疑。

## Git使用说明与学习资源推荐

### GitHub仓库网址

[GitHub - CS-STA: 计科协开源学习项目](https://github.com/0gaowei/CS-STA)

### 协作模式

本项目为开源社区项目，基于Git进行开源协作。各个方向的组长拥有直接`push`的权限，同时负责审核计科协小组成员或者社区成员的各个方向的`PR`请求和`issue`议题。计科协小组成员和社区成员通过发起PR请求发起贡献。

### Git学习资源

- Git基本原理：[Git + GitHub 10分钟完全入门_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1KD4y1S7FL/?spm_id_from=333.337.search-card.all.click&vd_source=ff10cd8f0b261d991b6d11019c48fbb2)
- Git进阶：[Git + GitHub 10分钟完全入门 (进阶)_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1hA411v7qX/?spm_id_from=333.1387.search.video_card.click&vd_source=ff10cd8f0b261d991b6d11019c48fbb2)
- 如何对开源项目进行共享：[给github项目贡献代码详细步骤_github上想给开源项目贡献源码 怎么做-CSDN博客](https://blog.csdn.net/u012443641/article/details/126344421)

## 计科协开源仓库CS-STA架构介绍

### 各方向学习资源仓库

组长负责管理资源的上传，或者审核他人资源上传的`PR`请求。资源分类存放，可以是各类文件（视频，ppt，pdf，或者是网址链接存到txt文件里都可以）。

### 各方向学习路径与学习笔记仓库

- 学习路径为`md`文件，说明要达到某个学习目标需要学习的资源或者完成的任务，资源可以是分方向学习资源仓库里的，也可以是网上的链接资源。由组长负责上传或者审核他人提交的`PR`请求。
- 学习笔记所有人都可以上传（发起`PR`请求）到对应方向的`note`文件夹里，推荐使用md格式，也可以是其他形式。

### Project项目仓库

用于存储各个方向的开源学习项目。遵循项目原有的协议，仅供学习使用。

## 各个仓库的贡献模板文档template.md说明

### 项目文档列表

#### 项目根目录

- **LICENSE**：项目的开源许可协议文件。
- **`README.md`**：项目的主介绍文档，通常包含项目概述、目标、架构、如何参与等内容。

#### 学习路径与笔记目录（learn_path_and_note）

- **LPN_README.md**：学习路径与笔记目录的说明文档。
- **roadmap_template.md**：学习路径模板文件，用于指导组长编写学习路径。
- **`**介绍.md`：**各方向学习路径与介绍,如`数模介绍.md`。

#### 学习资源目录（learn_src）

- **LS_README.md**：学习资源目录的说明文档。
- **src_list_template.md**：学习资源列表模板文件，用于指导成员编写学习资源清单。
- **`**src_list.md`：**各方向学习资源清单**,如`数模学习src_list.md`。

#### 项目目录（project）

- **PRJCT_README.md**：项目目录的说明文档。
- **demo_project_readme_template.md**：示例项目的README模板文件，用于指导成员编写项目文档。

## 面向CS-STA组员与社区成员的项目贡献指南

> 请务必遵循各个仓库的Readme.md的模板要求。

1. Fork仓库：Fork项目的GitHub仓库到自己的账户。
2. 克隆仓库：将Fork的仓库克隆到本地。
3. 创建分支：创建一个新的分支进行开发。
4. 提交更改：在本地进行开发后，提交更改到分支。
5. Pull Request：向主仓库提交Pull Request，等待各个方向组长审核和合并。

如果发现项目出现问题，或者学习资源失效等其他问题，开源发起GitHub Issues：通过GitHub Issues提交问题和建议。
若有其他问题可以邮箱联系：0gaowei@gmail.com

本项目仅供学习使用，若有侵权请联系删除。
