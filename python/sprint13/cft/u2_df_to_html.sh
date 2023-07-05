#!/bin/bash
# ------------------------------
# 20230705 8.10 begin
# ------------------------------
X=90
#limit space for system

echo 'Begin my script' > result.txt
echo ' ' >> result.txt

#example
# <table> 
#     <tr>
#         <th>User</th>
#         <th>Count</th>
#         <th>Color</th>
#     </tr>
#      <tr><td>User1</td><td>11</td><td>Red</td></tr> 
#      <tr><td>User2</td><td>3</td><td>Green</td></tr> 
# </table>


# caption="hostname -A = $(hostname -A)$(hostname -I)"
# caption="$(hostname -A)$(hostname -I)"

echo '<table>' > result.txt
caption="hostname -A = $(hostname -A)"
echo '<br><big>'$caption'<br></big>' >> result.txt
caption="hostname -I = $(hostname -I)"
echo '<br><big>'$caption'<br></big>' >> result.txt
echo '<br><big>'limit space for system = $X %'<br></big>' >> result.txt
echo '<br><big><i>#df -h</i></big>' >> result.txt

# echo '<caption><br><big>'$caption'<br><br></big></caption>' >> result.txt

echo '<tr><th>Filesystem</th><th>Size</th><th>Used</th><th>Avail</th><th>Use%</th><th>Mounted on</th></tr>' >> result.txt


declare -a list_mounts

send_status='green'
list_mounts=($(df -h |awk '{print $6}'))
# list_use_spaces=($(df -h |awk '{print $5}'| sort -u|tr -d "%"))
# list_users=($(ps -fA | awk '{print $1}'| sort -u ))

for i in "${list_mounts[@]}"
do
    # echo ' ' >> result.txt
    # if [ $i = 'Mounted' ];
    if [[ $i != /* ]];
        then
            # echo 'UID continue' >> result.txt
            continue
    fi
    # echo $i >> result.txt
    # count_space=$(ps -fA | awk '{print $1}' | grep -c $i)
    # echo $count_proc >> result.txt
    # sum=$(($count_proc+$X))
    # echo $sum >> result.txt
    Filesystem=$(df -h | awk '{ if ($6 == "'$i'") print $1}')
    Size=$(df -h | awk '{ if ($6 == "'$i'") print $2}')
    Used=$(df -h | awk '{ if ($6 == "'$i'") print $3}')
    Avail=$(df -h | awk '{ if ($6 == "'$i'") print $4}')
    Use=$(df -h | awk '{ if ($6 == "'$i'") print $5}'|tr -d "%")
    Mounted=$(df -h | awk '{ if ($6 == "'$i'") print $6}')
    
    # Filesystem            Size  Used Avail Use% Mounted on
    # echo $i >> result.txt
    # echo $Filesystem >> result.txt
    # echo $Use >> result.txt

    if [ $Use -lt $X ];
        then
            echo '<tr><td>'$Filesystem'</td><td>'$Size'</td><td>'$Used'</td><td>'$Avail'</td><td bgcolor="green">'$Use'</td><td>'$Mounted'</td></tr>' >> result.txt
        else
            send_status='red'
            echo '<tr><td>'$Filesystem'</td><td>'$Size'</td><td>'$Used'</td><td>'$Avail'</td><td bgcolor="red">'$Use'</td><td>'$Mounted'</td></tr>' >> result.txt
    fi
done
echo '</table>' >> result.txt
# echo $send_status >> result.txt
bash send.sh 192.168.100.101 1984 "status user02.hm2 $send_status `date` `cat result.txt`"
