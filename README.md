# AI工作台
基于 PySide6 + LangChain + 智谱 GLM 大模型开发的多功能 AI 桌面应用

## 项目介绍
这是一个带图形界面的 AI 工具，支持通用对话、代码生成、AI 绘图提示词、文本翻译等功能，支持明暗主题切换、配置自定义、历史记录管理。

## 功能特性
- 多场景 AI 模型切换：通用对话 / 代码助手 / 文生图 / 翻译
- 支持深色 / 浅色主题自由切换
- 自定义 API Key、模型版本、界面风格
- 实时聊天 + 历史记录查看
- 可视化图形交互界面，操作简单

## 技术栈
- Python
- PySide6（GUI 界面）
- LangChain（大模型调用）
- 智谱 AI ChatGLM（大模型）

### 环境依赖
Python 3.8+
安装依赖：
pip install -r requirements.txt

### 使用说明
1. 在keys.py中填入个人智谱AI API密钥
2. 运行main.py启动程序

### 技术栈
Python | PySide6 | LangChain | ChatGLM

## 运行方法
1. 安装依赖
2. 在 `keys.py` 中填入你的智谱 AI API Key
3. 运行程序

## 项目结构
- main.py        主程序入口
- stats2.py      UI 界面文件
- keys.py        API 密钥配置
- requirements.txt  依赖环境
