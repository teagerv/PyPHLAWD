import os
import sys
import tree_reader
from get_subset_genbank import make_files_with_id as mfid
from get_subset_genbank import make_files_with_id_internal as mfid_in
from get_subset_genbank import make_files_with_id_justtable as mfid_justtable

if __name__ == "__main__":
    if len(sys.argv) != 5 and len(sys.argv) != 6:
        print("python "+sys.argv[0]+" tree dir DB gzfileloc [limitlist]")
        sys.exit(0)
    
    tree = next(tree_reader.read_tree_file_iter(sys.argv[1]))
    dirl = sys.argv[2]
    if dirl[-1] != "/":
        dirl = dirl + "/"
    DB = sys.argv[3]
    
    gzfileloc = sys.argv[4]

    taxalist = None
    if len(sys.argv) == 6:
        taxalistf = open(sys.argv[5],"r")
        taxalist = set()
        for i in taxalistf:
            taxalist.add(i.strip())
        taxalistf.close()
    didntmake = set()
    for i in tree.iternodes():
        if "unclassified" in i.label:
            didntmake.add(i)
            continue
        if "environmental" in i.label:
            didntmake.add(i)
            continue
        if i.parent in didntmake:
            didntmake.add(i)
            continue
        orig = i.label
        if i != tree:
            i.label = i.parent.label+"/"+i.label
        tid = orig.split("_")[-1]
        dirr = i.label
        if len(i.children) == 0:
            mfid(tid,DB,dirl+dirr+"/"+orig+".fas",dirl+dirr+"/"+orig+".table",gzfileloc,True,limitlist = taxalist) 
        else:
            mfid_in(tid,DB,dirl+dirr+"/"+orig+".fas",dirl+dirr+"/"+orig+".table",gzfileloc,True,limitlist = taxalist) 
