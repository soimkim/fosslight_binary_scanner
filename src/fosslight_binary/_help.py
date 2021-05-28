#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 LG Electronics Inc.
# SPDX-License-Identifier: Apache-2.0
from fosslight_util.help import PrintHelpMsg

_HELP_MESSAGE_BINARY = """
    Usage: fosslight_bin [option1] <arg1> [option2] <arg2>...

    After extracting the binaries, the open source and license information of the saved binaries are retrieved by comparing the similarity
    with the binaries stored in the LGE Binary DB (FOSSLight > Binary DB) with the Binary's TLSH (Trend micro Locality Sensitive Hash).

    Mandatory:
        -p <binary_path>\t\t    Path to analyze binaries

    Options:
        -h\t\t\t\t    Print help message
        -a <target_architecture>\t    Target Architecture(x86-64, ARM, MIPS, Mach-O, and etc.)
        -o <output_path>\t\t    Path to save output files
        -f <customized_file_name>\t    Output file name(Automatically generated 'binary.txt')"""


def print_help_msg():
    helpMsg = PrintHelpMsg(_HELP_MESSAGE_BINARY)
    helpMsg.print_help_msg(True)
