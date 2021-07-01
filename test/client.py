#!/usr/bin/python3
# -*- coding: utf-8; mode: python -*-

import os
import sys
import Ice

Ice.loadSlice('-I /usr/share/slice /usr/share/slice/dharma/scone-wrapper.ice --all')
import Semantic


class client (Ice.Application):
    def run(self, argv):
        proxy = self.communicator().stringToProxy(argv[1])
        scone = Semantic.SconeServicePrx.uncheckedCast(proxy)

        if not scone:
            raise RuntimeError('Invalid proxy')

        print(scone.sentence('(is-x-a-y? {elephant} {mammal})'))

        return 0


sys.exit(client().main(sys.argv))
