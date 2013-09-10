class MatrixGenerator:
	
	data = "";
	features = ['s', 'b', 'w'];	#To be retrived by feature generator
	fm = [0, 0, 0];
	
	def __init__(self, data):
		MatrixGenerator.data = data
	
	def getMatrix(self):
		for index in range(len(MatrixGenerator.data)):
			c = MatrixGenerator.data[index];

			for x in range(len(MatrixGenerator.features)):
				if(c == MatrixGenerator.features[x]):
					MatrixGenerator.fm[x] += 1;
	
		return MatrixGenerator.fm

