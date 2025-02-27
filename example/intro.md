The file versa.lpf is a Location Constraint File (LPF) used in Lattice Diamond for defining pin assignments and electrical constraints for the Lattice ECP5 Versa FPGA.
    - Without this file, the FPGA tools won't know which pins to connect your design to.
    - During synthesis and place-and-route, this file is referenced to correctly assign signals to physical FPGA pins.
    - LPF describes the physical connections between your design and the outside world (e.g., which pins connect to the LEDs, clock, or display).
    - The LOCATE command is used to assign a logical signal to a physical pin on the FPGA. eg: LOCATE COMP "clk" SITE "P3";
    - COMP refers to a signal or module in your design. It represents a logical name in your Verilog/VHDL code that is being mapped to a physical pin on the FPGA. eg: LOCATE COMP "led[0]" SITE "E16";
    - IOBUF (I/O Buffer) specifies the I/O type and electrical properties of an FPGA pin.
    - The SITE keyword refers to the physical pin location on the FPGA. It defines which pin a logical signal is connected to.


