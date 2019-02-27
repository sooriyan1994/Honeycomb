import math
import os
from subprocess import Popen

#a = input('Enter the edge length of hexagon RCU: ')

#alpha = .5 * math.radians(angle)
#X = 5. * math.cos(alpha)
#Y = 5. * math.sin(alpha)

#f = open('param.py','w')
#f.write('alpha = ' + str(alpha) + '\n')
#f.write('X = ' + '%.6f' % round(X, 6) + '\n')
#f.write('Y = ' + '%.6f' % round(Y, 6) + '\n')
#f.write('MaxSize = 10.\n')
#f.write('LocSize = 1.\n')
#f.close()

SALOME_ROOT='/INSTALLABLES/salome_meca-2017/appli_V2017.0.2/bin/salome'
ASTER_ROOT='/INSTALLABLES/aster'
WORKING_DIR='/home/u1449908/Salome_files/new_hex'
ASTER_VERSION='2017.0.2'
MESH_NAME='hex_mesh.med'
COMM_FILE='hex_new.comm'

salome_run = Popen(SALOME_ROOT + ' -t -u ' + WORKING_DIR + '/hex_new.py', shell='TRUE')
salome_run.wait()

exportfile = os.path.join(WORKING_DIR,'hex_new.export')
e = open(exportfile,'w')
e.write('P actions make_etude\n')
e.write('P memjob 524288\n')
e.write('P memory_limit 4096.0\n')
e.write('P mode interactif\n')
e.write('P mpi_nbcpu 1\n')
e.write('P mpi_nbnoeud 1\n')
e.write('P ncpus 1\n')
e.write('P platform LINUX64\n')
e.write('P proxy_dir /tmp\n')
e.write('P rep_trav /tmp/case1\n')
e.write('P origine AsterStudy ' + ASTER_VERSION + '\n')
e.write('P version stable\n')
e.write('A args\n')
e.write('A memjeveux 512.0\n')
e.write('A tpmax 900\n')
e.write('F mmed '+ WORKING_DIR + '/' + MESH_NAME + ' D 20\n')
e.write('F comm '+ WORKING_DIR + '/' + COMM_FILE + ' D  1\n')
e.write('F rmed '+ WORKING_DIR + '/hex.rmed R  80\n')
e.write('F mess '+ WORKING_DIR + '/hex.mess R  6\n')
e.close()

aster_run = Popen(ASTER_ROOT + '/bin/as_run ' + WORKING_DIR + '/hex_new.export', shell='TRUE')
aster_run.wait()



#P nomjob RunCase_3_Stage_1
#P origine AsterStudy 2017.0.2
#P studyid 24904-0005-INPUNHADHPCSRV

#P tpsjob 16
#P version stable


#R base base-stage1 RC 0
