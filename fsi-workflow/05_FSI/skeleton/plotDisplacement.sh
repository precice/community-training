#! /bin/bash
gnuplot -p << EOF
set grid
set title 'Displacement of the wing Tip'
set xlabel 'Time [s]'
set ylabel 'Y-Displacement [m]'
# set style line 1 lt 2 lw 6
# set style line 1 lt 2 lw 6
# set linestyle  2 lt 2 lc 1 # red-dashed
# set linestyle  1 lt 2 lc 1 # red-dashed
plot "./precice-Solid-watchpoint-tip.log" using 1:9 title "tip" with lines, \
     "./precice-Solid-watchpoint-trailing.log" using 1:9 title 'tip TE' with lines, \
     "./precice-Solid-watchpoint-leading.log" using 1:9 title "tip LE" with lines, \
     "./precice-Solid-watchpoint-root-trailing.log" using 1:9 title "root TE" with lines, \
    "./precice-Solid-watchpoint-root-leading.log" using 1:9 title "root LE" with lines     
EOF

