{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# mode median and mean\n",
    "\n",
    "X = list()\n",
    "N = input()\n",
    "elements = input()\n",
    "\n",
    "for elem in elements.split(' '):\n",
    "    X.append(int(elem))c\n",
    "\n",
    "def mean(X=list()):\n",
    "    sum=0\n",
    "    for i in X:\n",
    "        sum=sum+i\n",
    "        i+1\n",
    "    mea= sum/len(X)\n",
    "    print(\"mean\" \"%.1f\" % mea)\n",
    "def median(X=list()):\n",
    "    X.sort()\n",
    "    if (len(X)% 2==0):\n",
    "        i=int(len(X)/2)\n",
    "        sum= (X[i]+X[i-1])/2\n",
    "        print(\"median:\" \"%.1f\" % sum)\n",
    "    else:\n",
    "        i=len(X)/2\n",
    "        print(\"median:\" \"%.1f\" % X[i])\n",
    "def mode(X=list()):\n",
    "    X.sort()\n",
    "    L1=[]\n",
    "    i = 0\n",
    "    while i < len(X): \n",
    "        L1.append(X.count(X[i])) \n",
    "        i += 1\n",
    "    d = dict(zip(X, L1))\n",
    "    for (i,j) in d.items():\n",
    "        print(\"{} : {}\".format(i,j))\n",
    "\n",
    "                     "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
