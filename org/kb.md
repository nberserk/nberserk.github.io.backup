# bash
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


* aws
** emr
- doesn't run when no default VPC is absent. https://aws.amazon.com/premiumsupport/knowledge-center/deleted-default-vpc/
- default vpc's 'DNS hostname' should be 'yes'. otherwise emr cluster will be terminated with error.

* avro
- http://avro.apache.org/docs/1.7.7/gettingstartedjava.html

* parquet
parquet은 columnar storage format


schema resolution
if the reader's record schema has a field that contains a default value, and writer's schema does not have a field with the same name, then the reader should use the default value from its field.
if the reader's record schema has a field with no default value, and writer's schema does not have a field with the same name, an error is signalled.

avro spec
https://avro.apache.org/docs/1.7.7/spec.html

- http://www.slideshare.net/cloudera/hadoop-summit-36479635?qid=ae3b9f6c-0e8d-4403-8048-46c1fe3a4b47&v=qf1&b=&from_search=3
  - size 33p, speed comparison 34p

convert existing data into parquet :  http://blog.cloudera.com/blog/2014/05/how-to-convert-existing-data-into-parquet/

1.4 parquet loading bug, https://issues.apache.org/jira/browse/SPARK-6566


// load and check column existence
val df = sqlContext.parquetFile("/test.parquet")
df.schema.fieldNames.contains("uidd")


* org
- file link (org-insert-link)
** babel
- insert code block. <s <tab>
- run code block; C-c C-c

* emacs
- C-x C-e ; eval lisp last lexpr
** artist mode
you can draw rectangle using ascii.
#+BEGIN_SRC lisp
;; enable mouse right button
(eval-after-load "artist"
   '(define-key artist-mode-map [(down-mouse-3)] 'artist-mouse-choose-operation)
   )
#+END_SRC

* spark sql
- subquery
#+BEGIN_SRC sql
select value, cnt from  ( select value, count(*) as cnt from user group by d order by d ) inner
where inner.c > 5
#+END_SRC

* jekyll
on El-Capitan
gem install --user-install --bindir ~/bin --no-document --pre --verbose jekyll

https://github.com/jekyll/jekyll/issues/3984

* git
- copy specific branch or tag to new git
old는 docker official git 이고, new는 비어있는 로컬 git.
#+BEGIN_SRC bash
git clone ssh://darren.ha@10.240.xx.xx:29418/docker
cd docker
git remote add github https://github.com/docker/docker.git
git fetch github
bit merge v1.10.2
git push origin master
#+END_SRC

* django
v 1.9
** model
Foreign Key vs OneToOneField : http://stackoverflow.com/questions/9949077/difference-between-foreignkeyuser-unique-true-and-onetoonefield


* angular2
editor : vs code rocks