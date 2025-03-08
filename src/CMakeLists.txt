add_library(soloud STATIC

    audiosource/ay/chipplayer.cpp
    audiosource/ay/sndbuffer.cpp
    audiosource/ay/sndchip.cpp
    audiosource/ay/sndrender.cpp
    audiosource/ay/soloud_ay.cpp
    audiosource/monotone/soloud_monotone.cpp
    audiosource/noise/soloud_noise.cpp
    audiosource/openmpt/soloud_openmpt.cpp
    audiosource/openmpt/soloud_openmpt_dll.c
    audiosource/sfxr/soloud_sfxr.cpp
    audiosource/speech/darray.cpp
    audiosource/speech/klatt.cpp
    audiosource/speech/resonator.cpp
    audiosource/speech/soloud_speech.cpp
    audiosource/speech/tts.cpp
    audiosource/tedsid/sid.cpp
    audiosource/tedsid/soloud_tedsid.cpp
    audiosource/tedsid/ted.cpp
    audiosource/vic/soloud_vic.cpp
    audiosource/vizsn/soloud_vizsn.cpp
    audiosource/wav/dr_impl.cpp
    audiosource/wav/soloud_wav.cpp
    audiosource/wav/soloud_wavstream.cpp
    audiosource/wav/stb_vorbis.c
    # backend/alsa/soloud_alsa.cpp
    # backend/coreaudio/soloud_coreaudio.cpp
    # backend/jack/soloud_jack.cpp
    # backend/miniaudio/soloud_miniaudio.cpp
    # backend/nosound/soloud_nosound.cpp
    # backend/null/soloud_null.cpp
    backend/openal/soloud_openal.cpp
    backend/openal/soloud_openal_dll.c
    # backend/opensles/soloud_opensles.cpp
    # backend/oss/soloud_oss.cpp
    # backend/portaudio/soloud_portaudio.cpp
    # backend/portaudio/soloud_portaudio_dll.c
    # backend/sdl/soloud_sdl1.cpp
    # backend/sdl/soloud_sdl1_dll.c
    # backend/sdl/soloud_sdl2.cpp
    # backend/sdl/soloud_sdl2_dll.c
    # backend/sdl2_static/soloud_sdl2_static.cpp
    # backend/sdl_static/soloud_sdl_static.cpp
    # backend/vita_homebrew/soloud_vita_homebrew.cpp
    # backend/wasapi/soloud_wasapi.cpp
    # backend/winmm/soloud_winmm.cpp
    # backend/xaudio2/soloud_xaudio2.cpp
    core/soloud.cpp
    core/soloud_audiosource.cpp
    core/soloud_bus.cpp
    core/soloud_core_3d.cpp
    core/soloud_core_basicops.cpp
    core/soloud_core_faderops.cpp
    core/soloud_core_filterops.cpp
    core/soloud_core_getters.cpp
    core/soloud_core_setters.cpp
    core/soloud_core_voicegroup.cpp
    core/soloud_core_voiceops.cpp
    core/soloud_fader.cpp
    core/soloud_fft.cpp
    core/soloud_fft_lut.cpp
    core/soloud_file.cpp
    core/soloud_filter.cpp
    core/soloud_misc.cpp
    core/soloud_queue.cpp
    core/soloud_thread.cpp
    c_api/soloud_c.cpp
    filter/soloud_bassboostfilter.cpp
    filter/soloud_biquadresonantfilter.cpp
    filter/soloud_dcremovalfilter.cpp
    filter/soloud_duckfilter.cpp
    filter/soloud_echofilter.cpp
    filter/soloud_eqfilter.cpp
    filter/soloud_fftfilter.cpp
    filter/soloud_flangerfilter.cpp
    filter/soloud_freeverbfilter.cpp
    filter/soloud_lofifilter.cpp
    filter/soloud_robotizefilter.cpp
    filter/soloud_waveshaperfilter.cpp
    # tools/codegen/main.cpp
    # tools/lutgen/main.cpp
    # tools/resamplerlab/main.cpp
    # tools/resamplerlab/stb_image_write.c
    # tools/sanity/sanity.cpp
)

target_include_directories(
    soloud
  PUBLIC $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
  PUBLIC $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include/soloud>)

add_library(soloud::soloud ALIAS soloud)