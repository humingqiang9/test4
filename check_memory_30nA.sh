#!/bin/bash

# 检查系统内存使用情况的脚本

echo "------------------------"
echo "系统内存使用情况报告"
echo "------------------------"
echo ""
echo "当前时间: $(date)"
echo ""

# 使用 free 命令获取内存信息，并以人类可读的单位显示
echo "1. 使用 free 命令查看内存:"
free -h
echo ""

# 使用 vmstat 命令查看虚拟内存统计信息
echo "2. 使用 vmstat 查看虚拟内存统计信息:"
vmstat -s
echo ""

# 检查 /proc/meminfo 文件获取更详细的内存信息
echo "3. 从 /proc/meminfo 获取详细信息:"
echo "总内存: $(grep MemTotal /proc/meminfo)"
echo "已用内存: $(grep MemFree /proc/meminfo)"
echo "可用内存: $(grep MemAvailable /proc/meminfo)"
echo ""

echo "报告生成完毕。"