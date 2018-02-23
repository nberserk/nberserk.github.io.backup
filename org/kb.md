# bash

```bash
bash -x script.sh # debug script
```

## strict mode

```bash
#!/bin/bash
set -euo pipefail
```

## if

```bash
    # checking first arg specified or not
    if [ -z "$1" ]; then
        folder=sparkjob
    else
        folder=$1
    fi

    #string compare
    s1='a'
    s2='b'
    if [ "$s1" = "$s2" ];  then
        echo "equal"
    else
        echo 'not equal'
    fi

    # integer compare
    s1=1
    s2=1
    if [ "$s1" -eq "$s2" ];  then
        echo "equal"
    else
        echo 'not equal'
    fi
```

```
| not   | equal |
| equal |       |
```

## nohup
DO NOT terminate background job, when i log off.

```bash
nohup ./script.sh < inputFile.txt > ./logFile 2>&1 &
nohup /path/to/command-name arg1 arg2 &
```

## sed
text replace tool. when used correctly, it's awesome!

```bash
echo 'day break' | sed 's/day/night/' # night break
sed -i 's/day/night/' org_file # substitute and save to file
sed -i 's:day:night/' org_file # just same with above. used different delimeter
sed -i '/^PATTERN/ s:.*:entire row changed' org_file # perform replace for PATTERN matching lines
sed -i "s/day/$MASTER/" org_file # replace with env var $MASTER
```

## split comma separated string

```bash
IFS=',' read -r -a array <<< "a,b,c"
for i in "${array[@]}"
do
    echo "$i"
done
```

## find script directory

```bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
```

## find

```bash
# ll under 1K files
find . -size -1k | xargs ls -l
#delete files samller than 1K
find . -size -1k -delete
```

## ssh, scp

```bash

scp -r conf s1:/usr/local/spark-1.3.0-bin-hadoop2.4/ # recursively copy directory to another machine
```

## encoding, iconv
iconv --from-code EUCKR in.file > out.file

# python

print("category=%s, url=%s, fn=%s" % (category, url, fn))

## getopt


