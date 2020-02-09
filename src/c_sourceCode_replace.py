# coding: utf-8

import sys
import math
import pandas as pd
import time
from sys import version_info
import csv
import re
import shutil
import logging

fmt = '%(asctime)s %(levelname)s %(name)s %(lineno)s %(message)s'
logging.basicConfig(level='DEBUG', format=fmt, filename='Rug.log', filemode='w')
syslogger = logging.getLogger('system')

class replace_operation():
    
    def __init__():
    
    @classmothod
    def set(target, substitute, source_file, output_file):
        replace_pattern = target
        
        #Regular expressions mean find the string follows target within a space
        #if combine reg-express should in this form
        actul_parameter_pattern = '(?<=\\b' + target + '\W)\w+'
        
        fake_function_call = substitute + ', @@@@)'
        output_line_result = []
        with open(source_file, encoding='utf-8') as file_obj:
            lineNum = 0
            for line in file_obj:
                re_replace_obj = re.compile(replace_pattern)
                re_value_obj = re.compile(actul_parameter_pattern)
                find = re.search(actul_parameter_pattern, line)
                if find:
                    actul_parameter = find.group()
                    #[example:] befor processing
                    
                    result_str = re.sub(replace_pattern, fake_function_call, line)
                    #[example:] after this processing
                    # replace target to substitute with a function calling form with fake parameter.
                    
                    result_str = re.sub(actul_parameter, '', result_str)
                    #[example:] after this processing
                    # remove actul parameter in code.
                    
                    result_str = re.sub(r'@@@@', actul_parameter, result_str)
                    #[example:] after this processing
                    # repalce fake parameter(@@@@) to actul parameter
                    
                    output_line_result.append(result_str)
                    continue
                output_line_result.append(line)
                lineNum+=1
                
        with open(output_file, 'w+') as file_object:
            for line in output_line_result:
                file_object.write(line)

    @classmothod
    def get(target, substitute, source_file, output_file):
        replace_get_pattern = target
        output_line_result = []
        with open(source_file, encoding='utf-8') as file_obj:
            lineNum = 0
            for line in file_obj:
                find = re.search(replace_get_pattern, line)
                if find:
                    value = find.group()
                    result_str = re.sub(replace_get_pattern, subsititute, line)
                    output_line_result.append(result_str)
                    continue
                output_line_result.append(line)
                lineNum+=1
                
        with open(output_file, 'w+') as file_object:
            for line in output_line_result:
                file_object.write(line)

    @classmothod
    def rep(target, substitute, source_file, output_file):
        #target should followed by space
        
        ''''
        better regular expression:
        [\S] means not white space for all. such as space, tab.
         \s  means white space.
        combination of " '[\S]' +target +'\s' " means no white space before target and white space follows target.
        '''
        replace_rep_pattern = '[\S]' +target + '\s' # better solution
        output_line_result = []
        with open(source_file, encoding='utf-8') as file_obj:
            lineNum = 0
            for line in file_obj:
                find = re.search(replace_get_pattern, line)
                if find:
                    value = find.group()
                    result_str = re.sub(replace_get_pattern, subsititute, line)
                    output_line_result.append(result_str)
                    continue
                output_line_result.append(line)
                lineNum+=1
                
        with open(output_file, 'w+') as file_object:
            for line in output_line_result:
                file_object.write(line)

if __name__ == "__main__":
    syslogger.info(sys.argv)
    if version_info.major !=3:
        raise Exception('Olny work on python 3.x')
    
    output_line_result = []
    output_line_result2 = []
    
    if(len(sys.arv) == 2):
        if '-v' in sys.argv:
            #PrintVersion()
        elif '-h' in sys.argv:
            PrintHelp()
            exit(0)
    
    if(len(sys.argv) != 3):
        syslogger.debug("Error operation")
        syslogger.debug("type -h for more information")
    else:
        mapping_file = '..\input\\' + sys.argv[1]
        source_file = '..\input\\' + sys.argv[2]
        output_file = '..\output\\' + sys.argv[2]
        syslogger.info('mapping_file: ' + mapping_file)
        syslogger.info('source_file: ' + source_file)
        syslogger.info('output_file: ' + output_file)
        
        csv_file = csv.reader(open(mapping_file, 'r'))
        for line in csv_file:
            syslogger.debug(line[0])
            operator = line[0]
            if 'set' == operator:
                replace_operation.set(line[1], line[2], source_file, output_file)
            elif 'get' == operator:
                replace_operation.get(line[1], line[2], source_file, output_file)
            elif 'rep' == operator:
                replace_operation.rep(line[1], line[2], source_file, output_file)
            else:
                syslogger.error('operater error')
            
            shutil.copyfile(output_file, source_file)
