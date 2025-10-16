{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNsGr8+vy8JW41YvbvihVEr",
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
        "<a href=\"https://colab.research.google.com/github/Sadiya-Akter-Mim/2nd_round_set_A/blob/main/q4_memory_bench_memory.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ps-On13zlcGP"
      },
      "outputs": [],
      "source": [
        "# bench_memory.py - simple simulation comparing allocation times (fixed-size pool vs python allocation)\n",
        "import time\n",
        "\n",
        "def slab_sim(num_alloc=20000, block_size=256):\n",
        "    pool = [bytearray(block_size) for _ in range(num_alloc//10)]\n",
        "    alloc_times = []\n",
        "    dealloc_times = []\n",
        "    for _ in range(num_alloc):\n",
        "        t0 = time.time()\n",
        "        if pool:\n",
        "            block = pool.pop()\n",
        "        else:\n",
        "            block = bytearray(block_size)\n",
        "        alloc_times.append(time.time()-t0)\n",
        "        t1 = time.time()\n",
        "        pool.append(block)\n",
        "        dealloc_times.append(time.time()-t1)\n",
        "    return alloc_times, dealloc_times\n",
        "\n",
        "def naive_sim(num_alloc=20000, block_size=256):\n",
        "    alloc_times = []\n",
        "    dealloc_times = []\n",
        "    holders = []\n",
        "    for _ in range(num_alloc):\n",
        "        t0 = time.time()\n",
        "        block = bytearray(block_size)\n",
        "        alloc_times.append(time.time()-t0)\n",
        "        holders.append(block)\n",
        "        t1 = time.time()\n",
        "        holders.pop()\n",
        "        dealloc_times.append(time.time()-t1)\n",
        "    return alloc_times, dealloc_times\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    print(\"Running slab simulation...\")\n",
        "    a1,d1 = slab_sim()\n",
        "    print(\"slab avg alloc (us):\", sum(a1)/len(a1)*1e6)\n",
        "    print(\"slab avg dealloc (us):\", sum(d1)/len(d1)*1e6)\n",
        "\n",
        "    print(\"Running naive simulation...\")\n",
        "    a2,d2 = naive_sim()\n",
        "    print(\"naive avg alloc (us):\", sum(a2)/len(a2)*1e6)\n",
        "    print(\"naive avg dealloc (us):\", sum(d2)/len(d2)*1e6)\n"
      ]
    }
  ]
}