#!/usr/bin/python
# -*- coding: cp949 -*-
"""
FFT Test code in python
"""

from pylab import *
from numpy.fft import fft, fftshift

Fs = 1000.  # the sampling frequency
Ts = 1. / Fs  # the sampling period

N = 256  # 샘플 갯수
freqStep = Fs / N  # resolution of the frequency in frequency domain

f = 10 * freqStep  # frequency of the wave
t = arange(N) * Ts  # x ticks in time domain, t = n*Ts
y = cos(2 * pi * f * t) + 0.5 * sin(2 * pi * 3 * f * t)  # 테스트 신호

Y = fft(y)  # FFT 분석
Y = fftshift(Y)  # middles the zero-point's axis

figure(figsize=(8, 8))
subplots_adjust(hspace=.4)

# Plot time data
subplot(3, 1, 1)
plot(t, y, '.-')
grid("on")
xlabel('Time (seconds)')
ylabel('Amplitude')
title('signals')
axis('tight')

freq = freqStep * arange(-N / 2, N / 2)  # x ticks in frequency domain

# Plot spectral magnitude
subplot(3, 1, 2)
plot(freq, abs(Y), '.-b')
grid("on")
xlabel('Frequency')
ylabel('Magnitude (Linear)')

# Plot phase
subplot(3, 1, 3)
plot(freq, angle(Y), '.-b')
grid("on")
xlabel('Frequency')
ylabel('Phase (Radian)')

show()
