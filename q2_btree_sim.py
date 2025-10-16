{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMrXmHNh3dutJ74/7hpQu70",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Sadiya-Akter-Mim/2nd_round_set_A/blob/main/q2_btree_sim.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "PWUEAOdPknmL"
      },
      "outputs": [],
      "source": [
        "# btree_sim.py - simple B-Tree for key -> pointer mapping (in-memory)\n",
        "class BTreeNode:\n",
        "    def __init__(self, t, leaf=False):\n",
        "        self.t = t\n",
        "        self.keys = []\n",
        "        self.values = []\n",
        "        self.children = []\n",
        "        self.leaf = leaf\n",
        "\n",
        "class BTree:\n",
        "    def __init__(self, t=3):\n",
        "        self.t = t\n",
        "        self.root = BTreeNode(t, True)\n",
        "\n",
        "    def search(self, k, x=None):\n",
        "        if x is None:\n",
        "            x = self.root\n",
        "        i = 0\n",
        "        while i < len(x.keys) and k > x.keys[i]:\n",
        "            i += 1\n",
        "        if i < len(x.keys) and x.keys[i] == k:\n",
        "            return x.values[i]\n",
        "        if x.leaf:\n",
        "            return None\n",
        "        return self.search(k, x.children[i])\n",
        "\n",
        "    def split_child(self, x, i):\n",
        "        t = self.t\n",
        "        y = x.children[i]\n",
        "        z = BTreeNode(t, y.leaf)\n",
        "        mid_key = y.keys[t-1]\n",
        "        mid_val = y.values[t-1]\n",
        "        z.keys = y.keys[t:]\n",
        "        z.values = y.values[t:]\n",
        "        y.keys = y.keys[:t-1]\n",
        "        y.values = y.values[:t-1]\n",
        "        if not y.leaf:\n",
        "            z.children = y.children[t:]\n",
        "            y.children = y.children[:t]\n",
        "        x.children.insert(i+1, z)\n",
        "        x.keys.insert(i, mid_key)\n",
        "        x.values.insert(i, mid_val)\n",
        "\n",
        "    def insert(self, k, v):\n",
        "        r = self.root\n",
        "        if len(r.keys) == 2*self.t -1:\n",
        "            s = BTreeNode(self.t, False)\n",
        "            s.children.insert(0, r)\n",
        "            self.root = s\n",
        "            self.split_child(s,0)\n",
        "            self._insert_nonfull(s, k, v)\n",
        "        else:\n",
        "            self._insert_nonfull(r, k, v)\n",
        "\n",
        "    def _insert_nonfull(self, x, k, v):\n",
        "        i = len(x.keys)-1\n",
        "        if x.leaf:\n",
        "            x.keys.append(None)\n",
        "            x.values.append(None)\n",
        "            while i>=0 and k < x.keys[i]:\n",
        "                x.keys[i+1] = x.keys[i]\n",
        "                x.values[i+1] = x.values[i]\n",
        "                i-=1\n",
        "            x.keys[i+1] = k\n",
        "            x.values[i+1] = v\n",
        "        else:\n",
        "            while i>=0 and k < x.keys[i]:\n",
        "                i-=1\n",
        "            i+=1\n",
        "            if len(x.children[i].keys) == 2*self.t -1:\n",
        "                self.split_child(x,i)\n",
        "                if k > x.keys[i]:\n",
        "                    i += 1\n",
        "            self._insert_nonfull(x.children[i], k, v)\n"
      ]
    }
  ]
}