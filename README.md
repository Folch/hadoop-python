A partir de les dades proporcionades al campus (vols realitzats en un any concret) hem de calcular la mitja de temps de delay de sortida per any i per aeroport.

Per provar el codi python sense necessitat d'executar-ho a través de hadoop podem fer:

`cat input/2007.csv | python mean/mapper.py | sort | python mean/reducer.py`

Comandes hadoop:
* Matar un procés: `hadoop job -kill <job_num>` 
* Copiar de local a hdfs: `hadoop fs -copyFromLocal local_file.txt path/hdfs/`
* Copiar de hdfs a local: `hadoop fs -copyToLocal path/hdfs/ path/local/`

Mirar el fitxer `exec_streaming.sh` per executar codi python a hadoop


