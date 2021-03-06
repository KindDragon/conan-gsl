from conans import ConanFile, CMake
import os


channel = os.getenv("CONAN_CHANNEL", "stable")
username = os.getenv("CONAN_USERNAME", "kinddragon")


class spdlogTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "gsl/0.0.1@%s/%s" % (username, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def imports(self):
        pass

    def test(self):
        os.chdir("bin")
        self.run(".%sexample" % os.sep)
