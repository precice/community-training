# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:52:35 2024

@author: claudio.caccia
"""


def convert_inp_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        in_node_section = False

        for line in lines:
            # Check if the line is the start of the node section
            if line.strip().startswith('*Node'):
                in_node_section = True
                file.write(line)
                continue

            # Check if the line is the start of another section
            if line.strip().startswith('*') and not line.strip().startswith('*Node'):
                in_node_section = False

            # Process lines within the node section
            if in_node_section and not line.strip().startswith('*'):
                parts = line.strip().split(',')
                if len(parts) == 4:
                    node_id = parts[0]
                    x = float(parts[1]) * 0.001
                    y = float(parts[2]) * 0.001
                    z = float(parts[3]) * 0.001
                    file.write(f'{node_id}, {x:.6f}, {y:.6f}, {z:.6f}\n')
                else:
                    file.write(line)
            else:
                file.write(line)


# Example usage
input_file = 'wing2312.inp'
output_file = 'wing2312_m.inp'
convert_inp_file(input_file, output_file)
