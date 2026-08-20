#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <cmath>
#include <iomanip>
#include <sstream>
#include <limits>

namespace {

constexpr double kCapacity = 60.0;
constexpr double kTargets[] = {30.0, 48.0, 60.0};  // 50%, 80%, 100%
constexpr int kSpeeds[] = {80, 100, 120};
constexpr int kConsume[] = {10, 14, 20};  // kWh / 100km
constexpr double kInf = std::numeric_limits<double>::infinity();
constexpr double kEps = 1e-9;

// Charge from `from` kWh to `to` kWh at station rate `rate` kW.
// Intervals [0,50%), [50%,80%), [80%,100%] use 100%, 80%, 10% of max rate.
double charge_time(double from, double to, double rate) {
    if (to <= from + kEps) {
        return 0.0;
    }
    const double levels[] = {0.0, 30.0, 48.0, 60.0};
    const double mult[] = {1.0, 0.8, 0.1};
    double time = 0.0;
    for (int i = 0; i < 3; ++i) {
        double lo = std::max(from, levels[i]);
        double hi = std::min(to, levels[i + 1]);
        if (hi > lo + kEps) {
            time += (hi - lo) / (rate * mult[i]);
        }
    }
    return time;
}

long long battery_key(double battery) {
    return llround(battery * 1000.0);  // 0.001 kWh precision for state key
}

struct State {
    int node;
    double battery;
    double time;

    bool operator>(const State& other) const { return time > other.time; }
};

}  // namespace

std::string win_time(std::vector<int>& infos) {
    /*
     * 返回结果四舍五入保留两位小数的字符串；小数位为 0 也要显示。
     * @param infos 第一个参数为起点到终点距离，第二个为服务区个数 n，
     *              后面 2n 个参数为：相对上一服务区（或起点）的距离、该服务区充电速度。
     * @return 从起点到终点所需最短时间（小时）
     */
    int total_distance = infos[0];
    int n = infos[1];

    std::vector<int> seg_dist(n + 1, 0);
    std::vector<double> station_rate(n, 0.0);
    int covered = 0;
    for (int i = 0; i < n; ++i) {
        seg_dist[i] = infos[2 + 2 * i];
        station_rate[i] = static_cast<double>(infos[2 + 2 * i + 1]);
        covered += seg_dist[i];
    }
    seg_dist[n] = total_distance - covered;  // last station -> end

    // nodes: 0 = start, 1..n = stations, n+1 = end
    const int end_node = n + 1;

    std::priority_queue<State, std::vector<State>, std::greater<State>> pq;
    std::map<std::pair<int, long long>, double> best;

    auto push_state = [&](int node, double battery, double time) {
        if (battery < -kEps) {
            return;
        }
        battery = std::min(battery, kCapacity);
        if (battery < 0) {
            battery = 0;
        }
        auto key = std::make_pair(node, battery_key(battery));
        auto it = best.find(key);
        if (it != best.end() && it->second <= time + kEps) {
            return;
        }
        best[key] = time;
        pq.push({node, battery, time});
    };

    push_state(0, kCapacity, 0.0);  // start with full battery

    double answer = kInf;

    while (!pq.empty()) {
        State cur = pq.top();
        pq.pop();

        auto key = std::make_pair(cur.node, battery_key(cur.battery));
        auto it = best.find(key);
        if (it != best.end() && cur.time > it->second + kEps) {
            continue;
        }

        if (cur.node == end_node) {
            answer = std::min(answer, cur.time);
            continue;
        }

        // Decide leaving battery after optional charging at current station.
        std::vector<std::pair<double, double>> leave_options;  // {battery, extra_time}
        leave_options.push_back({cur.battery, 0.0});           // no charge

        if (cur.node >= 1 && cur.node <= n) {
            double rate = station_rate[cur.node - 1];
            for (double target : kTargets) {
                if (target > cur.battery + kEps) {
                    leave_options.push_back(
                        {target, charge_time(cur.battery, target, rate)});
                }
            }
        }

        int seg = cur.node;  // segment from node -> node+1
        int dist = seg_dist[seg];
        if (dist < 0) {
            continue;
        }

        for (const auto& opt : leave_options) {
            double leave_battery = opt.first;
            double time_after_charge = cur.time + opt.second;

            for (int s = 0; s < 3; ++s) {
                double need = dist * (kConsume[s] / 100.0);
                if (leave_battery + kEps < need) {
                    continue;
                }
                double drive_time = static_cast<double>(dist) / kSpeeds[s];
                push_state(cur.node + 1, leave_battery - need,
                           time_after_charge + drive_time);
            }
        }
    }

    if (!std::isfinite(answer)) {
        return "Impossible";
    }

    // 加 1e-9 补偿浮点累积误差，保证恰好落在 .xx5 边界的值按四舍五入进位。
    double cents = std::floor(answer * 100.0 + 0.5 + 1e-9);
    std::ostringstream oss;
    oss << std::fixed << std::setprecision(2) << cents / 100.0;
    return oss.str();
}

int main() {
    // Example: no stations, 100 km -> best is 120 km/h => 100/120 ≈ 0.83 h
    // {
    //     std::vector<int> infos = {100, 0};
    //     std::cout << win_time(infos) << '\n';
    // }

    // One station: start --400--> station(rate=60) --300--> end, total 700
    {
        std::vector<int> infos = {600, 1, 500, 10};
        std::cout << win_time(infos) << '\n';
    }
    return 0;
}
