hadoop fs -rm -r mean/*
hadoop fs -copyFromLocal mean/* mean/
hadoop fs -rm -r output

hadoop jar lib/hadoop-streaming-2.6.0.jar \
        -file mean/mapper.py    -mapper mean/mapper.py \
        -file mean/reducer.py   -reducer mean/reducer.py \
        -input input -output output \
	-numReduceTasks 1 

rm -rf output/
hadoop fs -copyToLocal output .
