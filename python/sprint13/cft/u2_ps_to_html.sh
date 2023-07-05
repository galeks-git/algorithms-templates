#!/bin/bash
# # ------------------------------
# # 20230703 8.00 begin
# # ------------------------------

# #ps -fA | awk '{print $1}' | sort -u > result.txt

# # ps -fA | awk '{print $1}' | grep -c root > result.txt

# # ps -fA | awk '
# # BEGIN{print "<table>"}
# # {printf("<sstr><td>%d</td><td>%s</td></tr>\n",$1,$2)}
# # END{print "</table>"}
# # ' > result.txt

# # ps -fA | awk '{print $1}' | sort -u  | awk '{ps -u $1}' > result.txt
# # myarr=($(ps -u kdride | awk '{ print $1 }'))
# # list_users=( 1 2 3)
# X=100
# #limit process for user

# echo 'Begin my script' > result.txt
# echo ' ' >> result.txt
# echo '<table>' >> result.txt
# # echo ${list_users[1]} > result.txt

# declare -a list_users

# list_users=($(ps -fA | awk '{print $1}'| sort -u ))

# for i in "${list_users[@]}"
# do
#     echo ' ' >> result.txt
#     # # :
#     # if [$i == 'UID'];
#     #     then
#     #         # echo 'if $i == 'UID'' >> result.txt
#     #         echo $i >> result.txt
#     #     else
#     #         # echo $i >> result.txt
#     #         echo $(ps -u $i ) >> result.txt
#     #         # $(ps -fA | awk '{print $1}'| sort -u ) >> result.txt
#     # fi
#     # :
#     # if [$i -eq UID];
#     # if [$i -eq UID];
#     if [ $i = 'UID' ];
#         then
#             echo 'UID continue' >> result.txt
#             continue
#     fi
#     echo $i >> result.txt
#     # echo $(ps -u $i ) >> result.txt
#     count_proc=$(ps -fA | awk '{print $1}' | grep -c $i)
#     echo $count_proc >> result.txt
#     sum=$(($count_proc+$X))
#     echo $sum >> result.txt


#     # if [ $(($count_proc)) -lt $X ];
#     # if [$(($count_proc -lt $X))];
#     if [ $count_proc -lt $X ];
#         then
#             echo 'green' >> result.txt
#         else
#             echo 'red' >> result.txt
#     fi



#     # echo $(ps -fA | awk '{print $1}' | grep -c $i) >> result.txt
#     # $(ps -fA | awk '{print $1}'| sort -u ) >> result.txt
#     # echo $(ps -u $i ) >> result.txt
# done

# # ------------------------------
# # 20230703 10.30 final
# # ------------------------------
# X=100
# #limit process for user

# echo 'Begin my script' > result.txt
# echo ' ' >> result.txt

# #example
# # <table> 
# #     <tr>
# #         <th>User</th>
# #         <th>Count</th>
# #         <th>Color</th>
# #     </tr>
# #      <tr><td>User1</td><td>11</td><td>Red</td></tr> 
# #      <tr><td>User2</td><td>3</td><td>Green</td></tr> 
# # </table>

# echo '<table>' > result.txt
# echo '<tr><th>User</th><th>Count</th><th>Color</th></tr>' >> result.txt

# declare -a list_users

# list_users=($(ps -fA | awk '{print $1}'| sort -u ))

# for i in "${list_users[@]}"
# do
#     # echo ' ' >> result.txt
#     if [ $i = 'UID' ];
#         then
#             # echo 'UID continue' >> result.txt
#             continue
#     fi
#     # echo $i >> result.txt
#     count_proc=$(ps -fA | awk '{print $1}' | grep -c $i)
#     # echo $count_proc >> result.txt
#     # sum=$(($count_proc+$X))
#     # echo $sum >> result.txt

#     if [ $count_proc -lt $X ];
#         then
#             echo '<tr><td>'$i'</td><td>'$count_proc'</td><td>Green</td></tr>' >> result.txt
#         else
#             echo '<tr><td>'$i'</td><td>'$count_proc'</td><td>Red</td></tr>' >> result.txt
#     fi
# done
# echo '</table>' >> result.txt

# ------------------------------
# 20230705 8.00 final
# ------------------------------
X=10
#limit process for user

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

echo '<table>' > result.txt
caption="hostname -A = $(hostname -A)"
echo '<br><big>'$caption'<br></big>' >> result.txt
caption="hostname -I = $(hostname -I)"
echo '<br><big>'$caption'<br></big>' >> result.txt
echo '<br><big>'limit process for user = $X'<br></big>' >> result.txt
echo '<br><big><i>#ps -fA</i></big>' >> result.txt

# caption="$(hostname -A)$(hostname -I)"

# echo '<table>' > result.txt
# echo '<caption><br><big>'$caption'<br><br></big></caption>' >> result.txt

# echo ' ' >> result.txt

echo '<tr><th>User</th><th>Count</th><th>Color</th></tr>' >> result.txt


declare -a list_users

send_status='green'
list_users=($(ps -fA | awk '{print $1}'| sort -u ))

for i in "${list_users[@]}"
do
    # echo ' ' >> result.txt
    if [ $i = 'UID' ];
        then
            # echo 'UID continue' >> result.txt
            continue
    fi
    # echo $i >> result.txt
    count_proc=$(ps -fA | awk '{print $1}' | grep -c $i)
    # echo $count_proc >> result.txt
    # sum=$(($count_proc+$X))
    # echo $sum >> result.txt

    if [ $count_proc -lt $X ];
        then
            echo '<tr><td>'$i'</td><td bgcolor="green">'$count_proc'</td><td>Green</td></tr>' >> result.txt
        else
            send_status='red'
            echo '<tr><td>'$i'</td><td bgcolor="red">'$count_proc'</td><td>Red</td></tr>' >> result.txt
    fi
done
echo '</table>' >> result.txt
# echo $send_status >> result.txt
bash send.sh 192.168.100.101 1984 "status user02.hm1 $send_status `date` `cat result.txt`"
