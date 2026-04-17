
import Parallel_Odor.params as params
import Parallel_Odor.bindict as bindict
import Parallel_Odor.grow as grow
import Parallel_Odor.gidfunc as gidfunc

mitrals = {}

def _pd(mgid, isec, x):
  try:
    m = mitrals[mgid]
  except KeyError:
    if gidfunc.ismitral(mgid):
      m = grow.genMitral(mgid)
    elif gidfunc.ismtufted(mgid):
      m = grow.genMTufted(mgid)
    mitrals[mgid] = m

  d = x * (len(m.dend[isec].points)-1)
  sec = m.dend[isec].parent
  while sec != m.soma[0]:
    d += len(sec.points)-1
    sec = sec.parent
  return d*20

def pd(gid):
  if gid % 2:
    gid += 1
  return _pd(*bindict.gid_dict[gid][:3])
