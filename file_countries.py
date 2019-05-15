# a program that creates files and stores conuntry names. For example, a.txt named file will be created if country name starts with A.

with open("countries.txt", "r") as f:
	lines = f.readlines()
	for line in lines:
		if line.startswith("A"):
			with open("a.txt", "w") as fa:
				fa.write(line+"\n")
		elif line.startswith("B"):
			with open("b.txt", "w") as fb:
				fb.write(line+"\n")
		elif line.startswith("C"):
			with open("c.txt", "w") as fc:
				fc.write(line+"\n")
		elif line.startswith("D"):
			with open("d.txt", "w") as fd:
				fd.write(line+"\n")
		elif line.startswith("E"):
			with open("e.txt", "w") as fe:
				fe.write(line+"\n")
		elif line.startswith("F"):
			with open("f.txt", "w") as ff:
				ff.write(line+"\n")
		elif line.startswith("G"):
			with open("g.txt", "w") as fg:
				fg.write(line+"\n")
		elif line.startswith("H"):
			with open("h.txt", "w") as fh:
				fh.write(line+"\n")
		elif line.startswith("I"):
			with open("i.txt", "w") as fi:
				fi.write(line+"\n")
		elif line.startswith("J"):
			with open("j.txt", "w") as fj:
				fj.write(line+"\n")
		elif line.startswith("K"):
			with open("k.txt", "w") as fk:
				fk.write(line+"\n")
		elif line.startswith("L"):
			with open("l.txt", "w") as fl:
				fl.write(line+"\n")
		elif line.startswith("M"):
			with open("m.txt", "w") as fm:
				fm.write(line+"\n")
		elif line.startswith("N"):
			with open("n.txt", "w") as fn:
				fn.write(line+"\n")
		elif line.startswith("O"):
			with open("o.txt", "w") as fo:
				fo.write(line+"\n")
		elif line.startswith("P"):
			with open("p.txt", "w") as fp:
				fp.write(line+"\n")
		elif line.startswith("Q"):
			with open("q.txt", "w") as fq:
				fq.write(line+"\n")
		elif line.startswith("R"):
			with open("r.txt", "w") as fr:
				fr.write(line+"\n")
		elif line.startswith("S"):
			with open("s.txt", "w") as fs:
				fs.write(line+"\n")
		elif line.startswith("T"):
			with open("t.txt", "w") as ft:
				ft.write(line+"\n")
		elif line.startswith("U"):
			with open("u.txt", "w") as fu:
				fu.write(line+"\n")
		elif line.startswith("V"):
			with open("v.txt", "w") as fv:
				fv.write(line+"\n")
		elif line.startswith("W"):
			with open("w.txt", "w") as fw:
				fw.write(line+"\n")
		elif line.startswith("X"):
			with open("x.txt", "w") as fx:
				fx.write(line+"\n")
		elif line.startswith("Y"):
			with open("y.txt", "w") as fy:
				fy.write(line+"\n")
		else:
			with open("z.txt", "w") as fz:
				fz.write(line+"\n")