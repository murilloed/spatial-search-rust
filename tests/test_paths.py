import unittest,random
from spatialsearch.core import search
class Tests(unittest.TestCase):
    def test_astar_matches_dijkstra_multiple_grids(self):
        rng=random.Random(7)
        for _ in range(10):
            b={(x,y) for x in range(8) for y in range(8) if rng.random()<.2} - {(0,0),(7,7)}
            a=search(8,8,b,(0,0),(7,7)); d=search(8,8,b,(0,0),(7,7),False)
            self.assertEqual(a['path'] is None,d['path'] is None)
            if a['path']:
                self.assertEqual(len(a['path']),len(d['path']))
                self.assertFalse(set(a['path'])&b)
                self.assertTrue(all(abs(u[0]-v[0])+abs(u[1]-v[1])==1 for u,v in zip(a['path'],a['path'][1:])))
    def test_unreachable(self): self.assertIsNone(search(3,3,[(1,0),(0,1)],(0,0),(2,2))['path'])
