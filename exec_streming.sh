/Users/alexpardo/tools/hd/hadoop/bin/hadoop jar /Users/alexpardo/tools/hd/hadoop-2.6.0/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
        -file mapper.py    -mapper mapper.py \
        -file reducer.py   -reducer reducer.py \
        -input wordcount/input/cat -output wordcount/output/cat & \
/Users/alexpardo/tools/hd/hadoop/bin/hadoop jar /Users/alexpardo/tools/hd/hadoop-2.6.0/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
        -file mapper.py    -mapper mapper.py \
        -file reducer.py   -reducer reducer.py \
        -input wordcount/input/en -output wordcount/output/en