# Project name
PROJ = blinky

# Constraint file
CONSTR = versa.lpf

# Trellis installation path (modify if installed elsewhere)
TRELLIS ?= /usr/local

# FPGA Device Parameters
DEVICE = --um-45k  # LFE5UM-45F
PACKAGE = --package CABGA381  # Package type

# Default target
all: ${PROJ}.bit

# Synthesize Verilog source using Yosys
%.json: %.v
	yosys -p "synth_ecp5 -top blinky -json $@" $<

# Place & route using nextpnr-ecp5
%_out.config: %.json
	nextpnr-ecp5 --json $< --lpf ${CONSTR} --textcfg $@ ${DEVICE} ${PACKAGE}

# Generate bitstream using ecppack
%.bit: %_out.config
	ecppack --svf-rowsize 100000 --svf ${PROJ}.svf $< $@

# Flash the FPGA using OpenOCD
prog: ${PROJ}.svf
	openocd -f ${TRELLIS}/misc/openocd/ecp5-versa5g.cfg -c "transport select jtag; init; svf $<; exit"

# Clean up generated files
clean:
	rm -f *.bit *.svf *_out.config *.json

.PHONY: all prog clean
.PRECIOUS: ${PROJ}.json ${PROJ}_out.config
