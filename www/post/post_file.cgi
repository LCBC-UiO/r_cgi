#!/usr/bin/env Rscript

dst_fn <- "/tmp/out_test1234.csv"

# read everything from stdin
d <- read.table(file("stdin"), sep=",")

# write to a new file
write.table(d, file=dst_fn)

# send header

# tell client that everything went fine
cat(sprintf("Status: 200\r\n"))
# what are we sending back?
cat(sprintf("Content-type: application/json\r\n"))
# end of header
cat(sprintf("\r\n"))

# send body

cat(sprintf('{ "message_from_r": "your table has been written to %s" }\n', dst_fn))
