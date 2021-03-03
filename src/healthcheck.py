# -*- coding: utf-8 -*-
# TODO description

import logging
import os

import psutil
from flask import jsonify

logger = logging.getLogger("healthcheck")


def check_health():
    healthcheck = HealthCheck()
    return jsonify(ok=healthcheck.is_ok(), _details=healthcheck.get_details())


def get_readable_CPU_usage():
    """ returns info about the CPU usage in a readable string"""
    healthcheck = HealthCheck()
    cpu = healthcheck.cpu
    readable_cpu_info = "CPU usage -"
    readable_cpu_info += f" free: {cpu['free']} GB"
    readable_cpu_info += f", used: {cpu['used']} GB"
    readable_cpu_info += f",  available: {cpu['available']} GB"
    readable_cpu_info += f", total: {cpu['total']} GB"
    return readable_cpu_info


def get_readable_memory_usage():
    """ returns info about the memory usage in a readable string"""
    healthcheck = HealthCheck()
    memory = healthcheck.memory
    readable_memory_info = "Memory usage -"
    readable_memory_info += f" free: {memory['free']} GB"
    readable_memory_info += f", used: {memory['used']} GB"
    readable_memory_info += f",  available: {memory['available']} GB"
    readable_memory_info += f", total: {memory['total']} GB"
    return readable_memory_info


def get_readable_disk_info():
    """ returns info about the disk usage in a readable string"""
    healthcheck = HealthCheck()
    disk = healthcheck.disk
    readable_disk_info = "Disk usage -"
    readable_disk_info += f" free: {disk['free']} GB"
    readable_disk_info += f", used: {disk['used']} GB"
    readable_disk_info += f", total: {disk['total']} GB"
    return readable_disk_info


class HealthCheck:
    def __init__(self):
        super().__init__()
        self.cpu = self.__get_cpu_info()
        self.memory = self.__get_memory_info()
        self.disk = self.__get_disk_info()

    def is_ok(self):
        return all(
            [
                # CPU usage is under 90%
                self.cpu["average_cpu_usage"] < 90.0,
                # We have at least 256MB of RAM available
                self.memory["available"] > 0.25,
                # We have at least 5.0GB of free space in disk
                self.disk["free"] > 5.0,
            ]
        )

    def get_details(self):
        return {
            "cpu": self.cpu,
            "memory": self.memory,
            "disk": self.disk
        }

    @staticmethod
    def __get_cpu_info():
        return {
            "average_cpu_usage": psutil.cpu_percent(),
            "per_cpu_usage": psutil.cpu_percent(percpu=True),
        }

    @staticmethod
    def __get_disk_info():
        disk_info = psutil.disk_usage(os.getcwd())

        return {
            "total": in_gigabytes(disk_info.total),
            "used": in_gigabytes(disk_info.used),
            "free": in_gigabytes(disk_info.free),
        }

    @staticmethod
    def __get_memory_info():
        memory = psutil.virtual_memory()

        return {
            "total": in_gigabytes(memory.total, 2),
            "available": in_gigabytes(memory.available, 2),
            "used": in_gigabytes(memory.used, 2),
            "free": in_gigabytes(memory.free, 2),
        }


def in_gigabytes(value_in_bytes, digits=1):
    gigabytes = 1024 ** 3
    return round(value_in_bytes / gigabytes, digits)
