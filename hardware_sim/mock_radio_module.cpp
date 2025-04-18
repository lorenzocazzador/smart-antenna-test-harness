#include <iostream>
#include <thread>
#include <chrono>
#include <string>

class MockRadioModule {
public:
    void initialize() {
        std::cout << "[Radio] Initialization complete.\n";
    }

    void align_antenna(bool inject_error = false) {
        std::cout << "[Radio] Antenna alignment in progress...\n";
        std::this_thread::sleep_for(std::chrono::seconds(1));
        if (inject_error) {
            std::cerr << "[Radio] Alignment failed due to mechanical fault.\n";
        } else {
            std::cout << "[Radio] Alignment successful.\n";
        }
    }

    void simulate_comm_loss() {
        std::cout << "[Radio] Signal lost. Attempting recovery...\n";
        std::this_thread::sleep_for(std::chrono::seconds(1));
        std::cout << "[Radio] Signal restored.\n";
    }
};

int main(int argc, char* argv[]) {
    MockRadioModule radio;
    radio.initialize();

    bool inject_error = false;
    std::string mode = "normal";

    if (argc > 1) {
        mode = argv[1];
    }
    if (argc > 2 && std::string(argv[2]) == "error") {
        inject_error = true;
    }

    if (mode == "align") {
        radio.align_antenna(inject_error);
    } else if (mode == "loss") {
        radio.simulate_comm_loss();
    } else {
        radio.align_antenna();
        radio.simulate_comm_loss();
    }

    return inject_error ? 1 : 0;
}
