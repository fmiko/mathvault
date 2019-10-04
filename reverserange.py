def reversed_range(start, stop=None, step=1):
  if stop is None:
    return range(start - step, -step, -step)
  else:
    new_start = stop - ((stop-start-1) % step + 1)
    new_end = new_start - (stop-start+step-1) // step * step
    if (stop - start) % step == 0 and step < 0: new_start -= step
    return range(new_start, new_end, -step)

print(reversed_range(1, 10, 2))

print(reversed_range(1, 5, 1))