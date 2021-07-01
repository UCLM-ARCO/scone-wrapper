// -*- mode: c++; coding: utf-8 -*-

module Semantic {

  exception SconeError { string reason; };
  exception FileError { string reason; };

  interface SconeService {
      string request(string request) throws SconeError;
      string sentence(string sentence) throws SconeError;
      // void checkpoint(string name) throws FileError;
    };
};
