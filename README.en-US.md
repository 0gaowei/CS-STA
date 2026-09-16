# XD-CS-STA Open Source Learning Plan

## Project Introduction

This project is a systematic open source learning plan. Learning directions sit at the repository root, with year (semester) directories underneath, covering several major technical fields. Through structured learning paths and resource management, learners can quickly get started in various technical fields.

### Project Goals

- **Quick Start**: Use systematic learning paths to quickly acquire knowledge in various technical directions and resolve the confusion of getting started.
- **Open Source Contribution**: Participate in the open sharing of learning resources to improve professional and communication skills.
- **Project Development**: Directly participate in the development of open source projects to accumulate project experience.
- **Competition Preparation**: Prepare for various competitions through project development.

### Project Roadmap

1. **Introduction to Directions**: Quickly get started in various technical directions through systematic learning paths.
2. **Open Source Project Secondary Development**: Participate in the secondary development of open source projects to accumulate project experience.
3. **Participation in Competitions**: Prepare for various competitions through project development.
4. **Capability Enhancement**: Improve personal abilities to prepare for future participation in scientific research.

### Learning Directions

This project supports learning in multiple technical directions, each with a detailed roadmap and resource management. The current main supported directions are:

- **AI**
  - **AI**: General introduction to AI and its sub-fields.
  - **Data Analysis**: Learn the basics of data mining, master tools such as Python, Numpy, and Pandas, learn machine learning algorithms, and perform data visualization analysis.
  - **Deep Learning**: Introduction to deep learning basics, learn models such as linear regression, logistic regression, and neural networks, and master the PyTorch framework.
- **DEV**
  - **DEV**: Learn computer network basics, master front-end and back-end development technologies, learn API design and database interaction, and build a personal blog project.
  - **Agent Applications**: Understand Agent concepts, learn to build Agent applications on the Coze platform, master basic Python syntax, and learn LLM API calls and Agent framework development.
  - **Game Development**: Introduction to Unity and related game development.
- **数模 (Mathematical Modeling)**: Understand the basics of mathematical modeling, learn various modeling methods, choose a professional role (Programmer/Writer/Modeler), and participate in competition training.
- **嵌入式 (Embedded Systems)**: Learn 51 MCU and STM32 development, master the Linux system, and perform hardware debugging and embedded application development.
- **ACM**: Introduction to algorithms and programming contests.
- **CTF**: Introduction to cybersecurity and capture-the-flag contests.

## Git Usage Instructions and Recommended Learning Resources

### GitHub Repository URL

[GitHub - CS-STA: Computer Science Student Association Open Source Learning Project](https://github.com/0gaowei/CS-STA)

### Collaboration Mode

This is an open source community project based on Git collaboration. Project maintainers have direct `push` permissions and are responsible for reviewing `PR` (Pull Request) requests and `issue` topics from community members across various directions. Community members contribute by initiating PR requests.

### Git Learning Resources

- Git Basic Principles: [Git + GitHub 10-Minute Complete Introduction_Bilibili](https://www.bilibili.com/video/BV1KD4y1S7FL/?spm_id_from=333.337.search-card.all.click&vd_source=ff10cd8f0b261d991b6d11019c48fbb2)
- Advanced Git: [Git + GitHub 10-Minute Complete Introduction (Advanced)_Bilibili](https://www.bilibili.com/video/BV1hA411v7qX/?spm_id_from=333.1387.search.video_card.click&vd_source=ff10cd8f0b261d991b6d11019c48fbb2)
- How to share open source projects: [Detailed steps to contribute code to a GitHub project - CSDN Blog](https://blog.csdn.net/u012443641/article/details/126344421)

## Project Architecture Introduction

### Project Structure

Learning directions live under `方向/`, at the same level as `docs/`, `project/`, and `templates/`. Children of a group are sub-tracks; the year folder goes under the sub-track. If a group has no split, the sub-track can reuse the group name (e.g. `方向/AI/AI`).

```text
方向/                                             # all learning directions
└── {Learning Direction}/                         # e.g. AI, DEV, 嵌入式, 数模, ACM, CTF
    └── {Sub-direction}/                          # e.g. AI, 深度学习, Agent应用
        └── {Year}/                               # e.g. 2025-spring, 2025-autumn
            ├── {Direction Name}Roadmap.md
            ├── learning-materials/
            └── report-records/
```

Cross-direction project artifacts are in `project/`, templates in `templates/`, general notes in `docs/`, and past-year semester overviews in `docs/往年说明/`.

### Learning Resource Management

- **learning-materials/**: Stores learning materials for each direction, including videos, PPTs, PDFs, code examples, etc.
- **report-records/**: Stores learners' weekly reports and progress records, organized by week.
- **Roadmap.md**: The learning roadmap for each direction, containing learning goals, resources, project practices, etc.

### Learning Path and Learning Notes

- The learning path is defined in the `Roadmap.md` file, explaining the resources to be studied or tasks to be completed to reach a specific learning goal.
- Learning notes and report records are stored in the `report-records/` directory; MD format is recommended.
- All learners can contribute learning resources and notes via PR requests.

### Project Repository

Used to store open source learning projects for each direction. Please follow the original project agreements; provided for learning purposes only.

## Project Contribution Guide

> Please be sure to follow the template requirements of the Readme.md in each respective repository.

1. **Fork Repository**: Fork the project's GitHub repository to your own account.
2. **Clone Repository**: Clone the forked repository to your local machine.
3. **Create Branch**: Create a new branch for development.
4. **Commit Changes**: After local development, commit changes to the branch.
5. **Pull Request**: Submit a Pull Request to the main repository and wait for the project maintainer to review and merge.

### Contribution Content

- **Learning Resources**: Upload high-quality learning materials to the `learning-materials/` directory.
- **Learning Notes**: Share learning notes in the `report-records/` directory.
- **Roadmap Optimization**: Improve the learning roadmaps for various directions.
- **Adding New Directions**: Add new learning directions and learning paths.
- **Feedback**: Submit issues and suggestions via GitHub Issues.

### Expansion Management

- **New Year Creation**: Create a new year directory under the relevant direction (e.g. `2026-spring`) to organize a new semester's plan.
- **Learning Direction Expansion**: Adding new learning directions is supported; create a new directory under `方向/` according to the standard structure.
- **Resource Migration**: Supports the migration and reuse of learning resources across different years.

## Contact Information

If you find any problems with the project or if learning resources have become invalid, please submit issues and suggestions via GitHub Issues.

This project is for learning purposes only. If there is any infringement, please contact us for removal.
