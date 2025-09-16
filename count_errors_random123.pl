#!/usr/bin/perl
use strict;
use warnings;

# 脚本功能：解析日志文件并统计错误次数
# 用法：perl script.pl <logfile>

# 检查命令行参数
my $logfile = $ARGV[0];
if (!$logfile) {
    die "错误: 请提供日志文件路径作为参数。\n用法: perl $0 <logfile>\n";
}

# 检查文件是否存在
unless (-e $logfile) {
    die "错误: 文件 '$logfile' 不存在。\n";
}

# 初始化错误计数器
my $error_count = 0;

# 打开文件
open(my $fh, '<', $logfile) or die "无法打开文件 '$logfile': $!";

# 逐行读取文件
while (my $line = <$fh>) {
    # 去除行尾的换行符
    chomp $line;
    # 检查行中是否包含 "ERROR" (不区分大小写)
    if ($line =~ /ERROR/i) {
        $error_count++;
        # 可选：打印包含错误的行
        # print "找到错误: $line\n";
    }
}

# 关闭文件
close $fh;

# 输出结果
print "在文件 '$logfile' 中找到的错误总数: $error_count\n";