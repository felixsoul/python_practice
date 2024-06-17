from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
print(type(X))

y = iris.target
print(type(y))

