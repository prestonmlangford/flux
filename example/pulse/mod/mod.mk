INC += -I$(call getdir,mod)

mod_src :=
mod_src += clock.m
mod_src += edge.m
mod_src += pulse.m

mod: $(call sources, mod, $(mod_src))
