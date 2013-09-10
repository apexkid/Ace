from data_handler import DataHandler
from matrix_generator import MatrixGenerator

c = DataHandler();
s = c.getData();
print s;

a = MatrixGenerator(s);
lis = a.getMatrix();

for index in range(len(lis)):
	print lis[index] 
