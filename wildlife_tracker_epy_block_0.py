"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, threshold=0.9, report_period=128):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Interval_Tagger',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.threshold = threshold
        self.my_log = gr.logger(self.alias())
        self.timer = 0
        self.report_period = report_period
        self.readyForTag = True


    def work(self, input_items, output_items):

        for index in range(len(input_items[0])):
            if input_items[0][index] > 0.95:
                key = pmt.intern('index')
                value = pmt.from_float(np.round(float(input_items[0][index]),2))
                writeIndex = self.nitems_written(0) + index-1
                #print(f"Index: {writeIndex}")
                #print(f"Value: {value}")            
                self.add_item_tag(0, writeIndex, key, value ) 

        output_items[0][:] = input_items[0]
        return len(output_items[0])
