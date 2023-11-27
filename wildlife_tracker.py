#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Wildlife Tracker
# Author: Derek Kozel
# GNU Radio version: 3.10.3.0

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import eng_notation
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import numpy as np
import wildlife_tracker_epy_block_0 as epy_block_0  # embedded python block
import wildlife_tracker_epy_block_1 as epy_block_1  # embedded python block



from gnuradio import qtgui

class wildlife_tracker(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Wildlife Tracker", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Wildlife Tracker")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "wildlife_tracker")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.variable_qtgui_entry_0 = variable_qtgui_entry_0 = 0
        self.samp_rate = samp_rate = int(2.4e6)
        self.pulse_len = pulse_len = 156
        self.min_freq = min_freq = 1000
        self.max_freq = max_freq = 2000

        ##################################################
        # Blocks
        ##################################################
        self._pulse_len_range = Range(1, 200, 1, 156, 200)
        self._pulse_len_win = RangeWidget(self._pulse_len_range, self.set_pulse_len, "Pulse Length (samples)", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._pulse_len_win)
        self._min_freq_tool_bar = Qt.QToolBar(self)
        self._min_freq_tool_bar.addWidget(Qt.QLabel("Min Tone Frequency" + ": "))
        self._min_freq_line_edit = Qt.QLineEdit(str(self.min_freq))
        self._min_freq_tool_bar.addWidget(self._min_freq_line_edit)
        self._min_freq_line_edit.returnPressed.connect(
            lambda: self.set_min_freq(eng_notation.str_to_num(str(self._min_freq_line_edit.text()))))
        self.top_layout.addWidget(self._min_freq_tool_bar)
        self._max_freq_tool_bar = Qt.QToolBar(self)
        self._max_freq_tool_bar.addWidget(Qt.QLabel("Max Tone Frequency" + ": "))
        self._max_freq_line_edit = Qt.QLineEdit(str(self.max_freq))
        self._max_freq_tool_bar.addWidget(self._max_freq_line_edit)
        self._max_freq_line_edit.returnPressed.connect(
            lambda: self.set_max_freq(eng_notation.str_to_num(str(self._max_freq_line_edit.text()))))
        self.top_layout.addWidget(self._max_freq_tool_bar)
        self._variable_qtgui_entry_0_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_entry_0_tool_bar.addWidget(Qt.QLabel("'variable_qtgui_entry_0'" + ": "))
        self._variable_qtgui_entry_0_line_edit = Qt.QLineEdit(str(self.variable_qtgui_entry_0))
        self._variable_qtgui_entry_0_tool_bar.addWidget(self._variable_qtgui_entry_0_line_edit)
        self._variable_qtgui_entry_0_line_edit.returnPressed.connect(
            lambda: self.set_variable_qtgui_entry_0(int(str(self._variable_qtgui_entry_0_line_edit.text()))))
        self.top_layout.addWidget(self._variable_qtgui_entry_0_tool_bar)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=16,
                taps=[],
                fractional_bw=0)
        self.qtgui_time_sink_x_2 = qtgui.time_sink_f(
            1024, #size
            585.9375, #samp_rate
            'Second time sink at end', #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_2.set_update_time(0.10)
        self.qtgui_time_sink_x_2.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2.enable_tags(True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(False)
        self.qtgui_time_sink_x_2.enable_grid(False)
        self.qtgui_time_sink_x_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_2.enable_control_panel(False)
        self.qtgui_time_sink_x_2.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_win = sip.wrapinstance(self.qtgui_time_sink_x_2.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_2_win)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(4, firdes.low_pass(1,samp_rate,samp_rate/(2*4), 1000), (-670280), samp_rate)
        self.fir_filter_xxx_0_0 = filter.fir_filter_ccc(8, firdes.low_pass(1,75e3,75e3/(2*4), 1000))
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(8, firdes.low_pass(1,600e3,600e3/(2*8), 1000))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.epy_block_1 = epy_block_1.blk(key_filter="index")
        self.epy_block_0 = epy_block_0.blk(threshold=0.5, report_period=128)
        self.epy_block_0.set_block_alias("index")
        self.blocks_wavfile_source_0 = blocks.wavfile_source('D:\\baseband_160991830Hz_10-45-33_26-11-2023 Rotoroa.wav', True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_peak_detector2_fb_0 = blocks.peak_detector2_fb(1, 100, 0.001)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_cc(pulse_len, 1, 4000, 1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.analog_pll_refout_cc_0 = analog.pll_refout_cc(0.35, (max_freq*2*np.pi/samp_rate), (min_freq*2*np.pi/samp_rate))


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_pll_refout_cc_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.blocks_char_to_float_0, 0), (self.epy_block_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_peak_detector2_fb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.blocks_wavfile_source_0, 1), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.epy_block_0, 0), (self.epy_block_1, 0))
        self.connect((self.epy_block_1, 0), (self.qtgui_time_sink_x_2, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.fir_filter_xxx_0_0, 0))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.analog_pll_refout_cc_0, 0))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_peak_detector2_fb_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_time_sink_x_2, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "wildlife_tracker")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_qtgui_entry_0(self):
        return self.variable_qtgui_entry_0

    def set_variable_qtgui_entry_0(self, variable_qtgui_entry_0):
        self.variable_qtgui_entry_0 = variable_qtgui_entry_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_entry_0_line_edit, "setText", Qt.Q_ARG("QString", str(self.variable_qtgui_entry_0)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_pll_refout_cc_0.set_max_freq((self.max_freq*2*np.pi/self.samp_rate))
        self.analog_pll_refout_cc_0.set_min_freq((self.min_freq*2*np.pi/self.samp_rate))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.low_pass(1,self.samp_rate,self.samp_rate/(2*4), 1000))

    def get_pulse_len(self):
        return self.pulse_len

    def set_pulse_len(self, pulse_len):
        self.pulse_len = pulse_len
        self.blocks_moving_average_xx_0.set_length_and_scale(self.pulse_len, 1)

    def get_min_freq(self):
        return self.min_freq

    def set_min_freq(self, min_freq):
        self.min_freq = min_freq
        Qt.QMetaObject.invokeMethod(self._min_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.min_freq)))
        self.analog_pll_refout_cc_0.set_min_freq((self.min_freq*2*np.pi/self.samp_rate))

    def get_max_freq(self):
        return self.max_freq

    def set_max_freq(self, max_freq):
        self.max_freq = max_freq
        Qt.QMetaObject.invokeMethod(self._max_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.max_freq)))
        self.analog_pll_refout_cc_0.set_max_freq((self.max_freq*2*np.pi/self.samp_rate))




def main(top_block_cls=wildlife_tracker, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
