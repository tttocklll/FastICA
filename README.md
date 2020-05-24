# FastICA (Independent Component Analysis) in Python

## What is ICA?
>Independent component analysis (ICA) is a computational method for separating a multivariate signal into additive subcomponents.
>(https://en.wikipedia.org/wiki/Independent_component_analysis)

## Algorithm
1. Center x
2. Whiten x
<img src="https://latex.codecogs.com/gif.latex?\tilde{x}&space;=&space;ED^{-\frac{1}{2}}E^Tx" />
where
**E** is an orthogonal matrix of eigenvectors.
**D** is a diagonalamtrix of eigenvalues.
3. Choose an initial value of **w** randomly
where
<img src="https://latex.codecogs.com/gif.latex?W&space;=&space;[\mbox{\boldmath&space;$w$}_1,&space;\mbox{\boldmath&space;$w$}_2,&space;\cdots,&space;\mbox{\boldmath&space;$w$}_n]" />
4. Compute new **w**
<img src="https://latex.codecogs.com/gif.latex?\mbox{\boldmath&space;$w$}_n^&plus;&space;=&space;E[\tilde{\mbox{\boldmath&space;$x$}}g(\mbox{\boldmath&space;$w$}_n^T\tilde{\mbox{\boldmath&space;$x$}})]-E[g^{\prime}(\mbox{\boldmath&space;$w$}_n^T\tilde{\mbox{\boldmath&space;$x$}})]\mbox{\boldmath&space;$w$}_n" />
where
<img src="https://latex.codecogs.com/gif.latex?g(x)&space;=&space;tanh(x)" />
5. Normalize new **w**
<img src="https://latex.codecogs.com/gif.latex?\mbox{\boldmath&space;$w$}_n=\frac{\mbox{\boldmath&space;$w$}_n^&plus;}{\left&space;\|&space;\mbox{\boldmath&space;$w$}_n^&plus;&space;\right&space;\|}" />
6. While **w** has not converged, return to 4. Check the convergence by computing
<img src="https://latex.codecogs.com/gif.latex?\left&space;|&space;\mbox{\boldmath&space;$w$}_{n,old}^T\mbox{\boldmath&space;$w$}_{n,new}&space;\right&space;|\simeq&space;1" />
7. Compute the dot product of **w** and **x** and you get **S**

## Example
<img src="myplot.png" />
