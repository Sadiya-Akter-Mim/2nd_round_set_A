{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPeIxdX84oumakseRCTuOxA",
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
        "<a href=\"https://colab.research.google.com/github/Sadiya-Akter-Mim/2nd_round_set_A/blob/main/q2_btree_test_btree.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "7eYxSYWvk3oG"
      },
      "outputs": [],
      "source": [
        "# test_btree.py\n",
        "from btree_sim import BTree\n",
        "bt = BTree(t=3)\n",
        "# simulate storing chunk_id -> pointer (string)\n",
        "for i in range(1,51):\n",
        "    bt.insert(i, f\"node://shard_{i%5}/chunk_{i}\")\n",
        "\n",
        "# test lookups\n",
        "print(\"Lookup 10:\", bt.search(10))\n",
        "print(\"Lookup 49:\", bt.search(49))\n",
        "print(\"Lookup 100 (none):\", bt.search(100))\n"
      ]
    }
  ]
}