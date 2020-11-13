#
# -*- coding:utf-8 -*-

# Author:smilida

from Bio import Entrez
#
Entrez.email = "515825813@qq.com"   ##always tell NCBI who you are
Entrez.tool = "LiteratureScript"

search_results = Entrez.read(Entrez.esearch(db="pubmed",
                                            term="Zea mays[ORGN] AND enhancer",
                                            reldate=1000,
                                            datetype="pdat",
                                            usehistory="y"))
count = int(search_results["Count"])
print("Found %i results" % count)

batch_size = 10
out_handle = open("Z.mays_enhancer_record.txt", "w")
for start in range(0, count, batch_size):
    end = min(count, start+batch_size)
    print("Going to download record %i to %i" % (start+1, end))
    fetch_handle = Entrez.efetch(db="pubmed",
                                 rettype="abstract",
                                 retmode="text",
                                 retstart=start,
                                 retmax=batch_size,
                                 webenv=search_results["WebEnv"],
                                 query_key=search_results["QueryKey"])
    data = fetch_handle.read()
    fetch_handle.close()
    out_handle.write(data)
out_handle.close()