def build_heap(data):
  swaps = []
  # try to achieve  O(n) and not O(n2)
  n = len(data)
  for i in range(n // 2 - 1, -1, -1):
    while True:
      min = i
      lChild = 2 * i + 1
      rChild = 2 * i + 2
      if data[lChild] < data[min]:
        min = lChild
      if data[rChild] < data[min]:
        min = rChild
      if i != min:
        data[i], data[min] = data[min], data[i]
        swaps.append((i, min))
      else:
        break
  check(n, data, swaps)
  return swaps


def check(n, data, swaps):
  for i in range(n // 2 - 1, -1, -1):
    lChild = 2 * i + 1
    rChild = 2 * i + 2
    if data[lChild] < data[i]:
      data[i], data[lChild] = data[lChild], data[i]
      swaps.append((i, lChild))
    if data[rChild] < data[i]:
      data[i], data[rChild] = data[rChild], data[i]
      swaps.append((i, rChild))
  return swaps


def main():
  # add another input for I or F
  # first two tests are from keyboard, third test is from a file
  txt = input()
  if "F" in txt:
    filename = input()
    if "a" not in filename:
      with open(str("test/" + filename), mode="r") as fails:
        n = int(fails.readline())
        data = list(map(int, fails.readline().split()))
    else:
      print("error")
  elif "I" in txt:
    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))
  else:
    print("Input error")

  # checks if lenght of data is the same as the said lenght
  assert len(data) == n

  # calls function to assess the data
  # and give back all swaps
  swaps = build_heap(data)

  # this number should be less than 4n (less than 4*len(data))
  # output all swaps
  print("swaps")
  print(len(swaps))
  for i, j in swaps:
    print(i, j)

if __name__ == "__main__":
  main()